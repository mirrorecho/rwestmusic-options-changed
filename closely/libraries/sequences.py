import math
import abjad
import calliope

from closely.libraries import rhythms, sequences

# TO DO: this is really useful! ... move to calliope!!!!
class PitchSequence(calliope.CalliopeBaseMixin):
    # TO DO: implement as either numbers or abjad pitch objects
    intervals = ()
    keep_in_range = None # set to tupe with start pitch, stop pitch
    transpose = 0 
    base_sequence = None
    base_selections = (0,1) # e.g. (0,1) would be same
    

    @property
    def cyclic_length(self):
        """returns the length after which sequence repeats (usu. on new start pitch)
        ...which is the least common multiple of the lengths of all the intervals and base selections up the chain"""
        from functools import reduce

        def get_lengths(my_sequence=None, lengths=()):
            my_lengths = lengths or []
            my_sequence = my_sequence or self
            if my_sequence.base_sequence:
                my_lengths.append(len(my_sequence.base_selections) - 1)
            if my_sequence.intervals:
                my_lengths.append(len(my_sequence.intervals) - 1)
            if my_sequence.base_sequence:
                return get_lengths(my_sequence.base_sequence, my_lengths)
            else:
                return my_lengths

        lengths = get_lengths(self)

        def my_gcd(*numbers):
            """return the greatest common divisor of the given integers"""
            from fractions import gcd
            return reduce(gcd, numbers)

        def lcm(a, b):
            """returns the lowest common multiple."""    
            return (a * b) // my_gcd(a, b)

        return reduce(lcm, lengths, 1)



    def cyclic_at(self, attr_name, index):
        my_tuple = getattr(self, attr_name)
        loop_length = len(my_tuple) - 1
        base_item = my_tuple[index % loop_length]
        return base_item + (my_tuple[-1] - my_tuple[0]) * (index // loop_length)

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

# TO DO !!!!!!!!!!!!!!!!!!!!!!!!! 
# THIS SHOULD BE DEPRECIATED IN FAVOR OF PhraseFactory BELOW!!!!!!!!!!!!!!!
# class PhraseMaker(calliope.CalliopeBaseMixin):
#     pitch_sequence = PitchSequence()
#     rhythm_pattern = rhythms.SymmetricalRhythmPattern()

#     def __init__(self, *args, **kwargs):
#         self.setup(**kwargs)

#     def get_phrase_cells(self, 
#             rhythm_lengths = (1,), 
#             pitch_sequence = None,
#             pitch_sequence_index=0, 
#             pitch_selections = None,
#             keep_in_range = None,
#             transpose=0,
#             fill_rests=False, 
#             ):
#         self.warn("PhraseMaker SHOULD BE DEPRECIATED")
#         cells = []
#         pitch_sequence = pitch_sequence or self.pitch_sequence
#         if pitch_selections:
#             pitch_sequence = pitch_sequence.select(*pitch_selections, keep_in_range=keep_in_range, transpose=transpose)
#         elif keep_in_range or transpose: 
#             pitch_sequence = pitch_sequence(keep_in_range=keep_in_range, transpose=transpose)
        
#         for rl in rhythm_lengths:
#             rhythm = self.rhythm_pattern(rl, fill_rests=fill_rests)
#             pitches_length = len(list(filter(lambda x: x>0, rhythm)))
#             cells.append(calliope.Cell(
#                 rhythm = rhythm,
#                 pitches = pitch_sequence[pitch_sequence_index : pitch_sequence_index+pitches_length],
#                 pitches_skip_rests = True
#             ))
#             pitch_sequence_index += pitches_length
#         return cells

#     # TO DO: possibly rethink / refactor ... DRY
#     def __call__(self, **kwargs):
#         return calliope.Phrase(*self.get_phrase_cells(**kwargs), **kwargs)

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


class PhraseFactory(calliope.Phrase):
        rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
        pitch_sequence = sequences.PITCH_SEQUENCE
        rhythm_lengths = (4,4)
        fill_rests = False
        rhythm_lengths = (1,) 
        pitch_sequence_index=0 
        pitch_selections = None
        keep_in_range = None
        transpose=0

        def get_pitch_sequence(self):
            pitch_sequence = self.pitch_sequence
            if self.pitch_selections:
                pitch_sequence = pitch_sequence.select(*self.pitch_selections, keep_in_range=self.keep_in_range, transpose=self.transpose)
            elif self.keep_in_range or self.transpose: 
                pitch_sequence = pitch_sequence(keep_in_range=self.keep_in_range, transpose=self.transpose)
            return pitch_sequence

        def set_children_from_class(self, *args, **kwargs):
            pitch_sequence = self.get_pitch_sequence()
            pitch_sequence_index = self.pitch_sequence_index
            
            for rl in self.rhythm_lengths:
                rhythm = self.rhythm_pattern(rl, fill_rests=self.fill_rests)
                pitches_length = len(list(filter(lambda x: x>0, rhythm)))
                self.append(calliope.Cell(
                    rhythm = rhythm,
                    pitches = pitch_sequence[pitch_sequence_index : pitch_sequence_index+pitches_length],
                    pitches_skip_rests = True
                ))
                pitch_sequence_index += pitches_length

        def reset_pitches(self):
            pitch_sequence = self.get_pitch_sequence()
            pitch_sequence_index = self.pitch_sequence_index
            for i, e in enumerate(self.non_rest_events):
                e.pitch = pitch_sequence[i + self.pitch_sequence_index]

class DronePhraseFactory(PhraseFactory):
    pitch_sequence = PitchSequence()

class TransformAddConstantPitch(calliope.Transform):
    pitch=0

    def transform_nodes(self, bubble):
        new_child = bubble[0](name=str(bubble.name) + "constant_pitch_" + str(self.pitch))
        for event in new_child.non_rest_events:
            event.pitch = self.pitch

        # print([e.pitch for e in new_child.events])

        bubble.append(new_child)