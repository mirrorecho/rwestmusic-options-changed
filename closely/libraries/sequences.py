import math
import abjad
import calliope
from closely.libraries.rhythms import SymmetricalRhythmPattern

# TO DO: this is really useful! ... move to calliope!!!!
class PitchSequence(calliope.CalliopeBaseMixin):
    # TO DO: implement as either numbers or abjad pitch objects
    intervals = ()
    keep_in_range = None # set to tupe with start pitch, stop pitch
    transpose = 0 
    base_sequence = None
    base_selections = (0,1,)


    def cyclic_at(self, attr_name, index):
        my_tuple = getattr(self, attr_name)
        loop_length = len(my_tuple) - 1
        base_item = my_tuple[index % loop_length]
        return base_item + (my_tuple[-1] - my_tuple[0]) * math.floor(index / loop_length) 

    def pitch_at(self, index):
        pitch = self.transpose
        if self.base_sequence:
            selected_index = self.cyclic_at("base_selections", index)
            pitch += self.base_sequence[selected_index]
        if self.intervals:
            pitch += self.cyclic_at("intervals", index)
        if self.keep_in_range:
            pitch_range = abjad.PitchRange.from_pitches(*self.keep_in_range)
            if pitch not in pitch_range:
                voiced_pitches = pitch_range.voice_pitch_class(pitch)
                if pitch < pitch_range.start_pitch.number:
                    pitch = voiced_pitches[0].number
                else:
                    pitch = voiced_pitches[-1].number
        return pitch


    def __init__(self, *intervals, **kwargs):
        self.intervals = intervals
        self.setup(**kwargs)

    def __getitem__(self, arg):
        if isinstance(arg, int):
            return self.pitch_at(arg)
        elif isinstance(arg, slice):
            start = arg.start or 0
            stop = arg.stop or 0
            step = arg.step or 1
            if start > stop and step > 0:
                step = 0 - step
            return tuple([self[i] for i in range(start, stop, step)])
        elif isinstance(arg, tuple):
            return tuple([self[a] for a in arg])
        else:
            raise IndexError('invalid index type')

    def __call__(self, *intervals, **kwargs):
        return PitchSequence(base_sequence=self, *intervals, **kwargs)

    def select(self, *selections, **kwargs):
        return PitchSequence(base_sequence=self, base_selections=selections, **kwargs)

PITCH_CELL = (0, 2, 3, 5)
PITCH_SEQUENCE = PitchSequence(*PITCH_CELL)
PITCH_SELECTIONS_G = (0,1,3,4,2,5)

class PhraseMaker(calliope.CalliopeBaseMixin):
    pitch_sequence = PitchSequence()
    rhythm_pattern = SymmetricalRhythmPattern()

    def __init__(self, *args, **kwargs):
        self.setup(**kwargs)

    # TO DO: possibly rethink / refactor ... DRY
    def __call__(self, 
            rhythm_lengths = (1,), 
            pitch_sequence = None,
            pitch_sequence_index=0, 
            pitch_selections = None,
            keep_in_range = None,
            transpose=0,
            fill_rests=False, 
            **kwargs
            ):
        cells = []
        pitch_sequence = pitch_sequence or self.pitch_sequence
        if pitch_selections:
            pitch_sequence = pitch_sequence.select(*pitch_selections, keep_in_range=keep_in_range, transpose=transpose)
        elif keep_in_range or transpose: 
            pitch_sequence = pitch_sequence(keep_in_range=keep_in_range, transpose=transpose)
        
        for rl in rhythm_lengths:
            rhythm = self.rhythm_pattern(rl, fill_rests=fill_rests)
            pitches_length = len(list(filter(lambda x: x>0, rhythm)))
            cells.append(calliope.Cell(
                rhythm = rhythm,
                pitches = pitch_sequence[pitch_sequence_index : pitch_sequence_index+pitches_length],
                pitches_skip_rests = True
            ))
            pitch_sequence_index += pitches_length
        return calliope.Phrase(*cells, **kwargs)

# EXAMPLE:
# pm = PhraseMaker(
#     pitch_sequence = PITCH_SEQUENCE.select(*PITCH_SELECTIONS_G, 
#         # keep_in_range=(0,11)
#         ),
#     rhythm_pattern = SymmetricalRhythmPattern(
#         pattern = ( (-1,), (0.5,0.5,) )
#         )
#     )
# p = pm(4,4,4,6)
# p.illustrate_me()



class TransformAddConstantPitch(calliope.Transform):
    pitch=0

    def transform_nodes(self, bubble):
        new_child = bubble[0](name=str(bubble.name) + "constant_pitch_" + str(self.pitch))
        for event in new_child.events:
            event.pitch = self.pitch
            for l in event:
                l.pitch = None # just to be safe

        print([e.pitch for e in new_child.events])

        bubble.append(new_child)