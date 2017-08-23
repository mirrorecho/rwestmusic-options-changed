import abjad
import calliope

PITCH_CELL = (0, 2, 3, 5)

class PitchSequence(calliope.CalliopeBaseMixin):
    # TO DO: implement as either numbers or abjad pitch objects
    pitch_cell = PITCH_CELL
    keep_in_range = None # set to tupe with start pitch, stop pitch
    start_transpose = 0

    def adjust_me(self, pitch):
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

    def __mul__(self, times):
        return [
            self.adjust_me( (p + self.pitch_cell[-1] * t) + self.start_transpose )
                for t in range(times) 
                    for p in self.pitch_cell[:-1] 
            ]

class CellsPhraseMaker(calliope.CalliopeBaseMixin):
    pitches = ()
    cell_pitch_selections = (0,1,3,4,2,5)

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