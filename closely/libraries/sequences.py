import math
import abjad
import calliope

# TO DO: this is really useful! ... move to calliope
class PitchSequence(calliope.CalliopeBaseMixin):
    # TO DO: implement as either numbers or abjad pitch objects
    pitch_cell = ()
    keep_in_range = None # set to tupe with start pitch, stop pitch
    transpose = 0

    def adjust_range(self, pitch):
        if self.keep_in_range:
            pitch_range = abjad.PitchRange.from_pitches(*self.keep_in_range)
            
            if pitch not in pitch_range:
                voiced_pitches = pitch_range.voice_pitch_class(pitch)
                if pitch < pitch_range.start_pitch.number:
                    pitch = voiced_pitches[0].number
                else:
                    pitch = voiced_pitches[-1].number
        
        return pitch

    def __init__(self, *args, **kwargs):
        if args:
            self.pitch_cell = args
        self.setup(**kwargs)

    def __getitem__(self, arg):
        loop_length = len(self.pitch_cell) - 1
        if isinstance(arg, int):
            basic_pitch = self.pitch_cell[arg % loop_length]
            return basic_pitch + self.transpose + self.pitch_cell[-1] * math.floor(arg / loop_length) 
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

PITCH_CELL = (0, 2, 3, 5)
PITCH_SEQUENCE = PitchSequence(*PITCH_CELL)

class CellsPhraseMaker(calliope.CalliopeBaseMixin):
    pitches = (0,)
    cell_pitch_selections = (0,)

    def __init__(self, *args, **kwargs):
        if args:
            self.pitch_cell = args
        self.setup(**kwargs)

    def __mul__(self, times):
        return calliope.Phrase(
                *[
                    calliope.Cell(
                        *[calliope.Event(
                            pitch = self.pitches[s + self.cell_pitch_selections[-1] * t],
                            beats = 1,
                            )
                            for s in self.cell_pitch_selections[:-1] 
                        ]
                    )
                    for t in range(times)
                ]
            )

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