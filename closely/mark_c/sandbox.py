import abjad
import calliope

from closely.libraries.sequences import PITCH_CELL, PitchSequence, CellsPhraseMaker

pitch_sequence_1a = PitchSequence() *2
pitch_sequence_1 = pitch_sequence_1a + pitch_sequence_1a[::-1]

class PhraseC_1(CellsPhraseMaker):
    pitches = pitch_sequence_1
    cell_pitch_selections = (0,1,2,2,3)


class PhraseC_Block(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10,12), (0,3,7,12), (0,5,10,12), (0,4,7,12), ) 
    line_1 = PhraseC_1()*2


# PhraseC_Block().illustrate_me()

# pitches_up_I = PitchSequence(*PITCH_CELL) * 5
# phrase_up_I = CellsPhraseMaker(pitches=pitches_up_I) * 3


# phrase_up_I.illustrate_me()