import abjad
import calliope

from closely.libraries.sequences import PITCH_CELL, PitchSequence, CellsPhraseMaker

pitch_sequence_1 = PitchSequence() * 2
# pitch_sequence_1 = pitch_sequence_1a  #+ pitch_sequence_1a[::-1]
# print(pitch_sequence_1)

class PhraseC1(CellsPhraseMaker):
    pitches = pitch_sequence_1
    cell_pitch_selections = (0,1,2,2,3)

class BlockC1(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10,12), (0,3,7,12), (0,5,10,12), (0,4,7,12), ) 
    line_c = PhraseC1() * 2 

block_c1 = BlockC1()
for line in block_c1:
    # print([c for c in line])
    for cell in reversed(line):
        new_cell = cell()
        new_cell[:] = new_cell[::-1]
        # print(len(new_cell))
        line.append(new_cell)
    # line.metrical_durations = ((4,4),)*4 # TO DO: this is a chintzy way to set metrical durations

calliope.illustrate_me(bubble=block_c1)


# pitches_up_I = PitchSequence(*PITCH_CELL) * 5
# phrase_up_I = CellsPhraseMaker(pitches=pitches_up_I) * 3


# phrase_up_I.illustrate_me()