import abjad
import calliope

from closely.libraries.sequences import PITCH_CELL, PitchSequence, CellsPhraseMaker, TransformAddConstantPitch

pitch_sequence_1a = PitchSequence() *2
pitch_sequence_1 = pitch_sequence_1a + pitch_sequence_1a[::-1]
pitch_root_1 = "C3"

class PhraseC_1(CellsPhraseMaker):
    pitches = pitch_sequence_1
    cell_pitch_selections = (0,1,2,2,3)


class PhraseC_1_Block(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10), (0,3,8), (0,4,7), (0,5,10), ) 
    line_1 = PhraseC_1()*2
    transform_add_pitch = TransformAddConstantPitch(pitch=-12)

phrase_c_1 = PhraseC_1_Block()
# phrase_c_1.append()
phrase_c_1_grid = calliope.PitchGrid.from_bubble(phrase_c_1)

phrase_c_1.illustrate_me()