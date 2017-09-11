import pandas as pd
import abjad
import calliope

from closely.libraries.sequences import PITCH_SEQUENCE, PitchSequence, CellsPhraseMaker, TransformAddConstantPitch

pitch_sequence_1 = PitchSequence()
pitch_root_1 = "C3"

class PhraseC1(CellsPhraseMaker):
    pitches = PITCH_SEQUENCE.select(0,1,2,2,3)

class BlockC1(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10), (0,3,7), (0,5,10), (0,4,7), ) 
    # TO DO: CONSIDER THESE INTERVALS:
    # intervals = ( (0,5,10), (0,3,8), (0,4,7), (0,5,10), ) 
    line_c = PhraseC1() * 2 
    transform_add_pitch = TransformAddConstantPitch(pitch=-12)

block_c1 = BlockC1(name="c1")
for line in block_c1:
    # print([c for c in line])
    for cell in reversed(line):
        new_cell = cell()
        new_cell[:] = new_cell[::-1]
        # print(len(new_cell))
        line.append(new_cell)
    # line.metrical_durations = ((4,4),)*4 # TO DO: this is a chintzy way to set metrical durations

def hill_range_maker(start, steps, increment=1, span=12):
    hill_range = [start + increment*i for i in range(steps)]
    hill_range += reversed(hill_range)
    return [(b, b+span) for b in hill_range]


# TO DO... standard way to initialize apps... and ignore existing files 
grid_c1 = calliope.PitchGrid.from_bubble(block_c1)
grid_c1.add_tally_apps(
        calliope.TallyCircleOfFifthsRange(over_range_multiplier=-99), 
        calliope.TallyParallelIntervals(interval_ratings=[(0,-20), (7,-11)]), 
        calliope.TallyMelodicIntervals(
                interval_ratings=[(0, -200), (1,40), (2,80), (3,60), (4,50), (5,6), (6,-20), (7,-4), (10,-30), (11,-50), (12,-4)], 
                over_incremental_multiplier=(12,-80),
                up_rating=-12,
                down_rating=20,
                ),
        calliope.TallyRepeatedJumps(),
    )
grid_c1.pitch_ranges = pd.DataFrame.from_records([
        hill_range_maker(8, 8, 2, 12), # flute
        hill_range_maker(-4, 8, 2, 12), # clarinet
        hill_range_maker(9, 8, -3, 12), # viola
        hill_range_maker(-3, 8, -3, 12), # cello
    ])
grid_c1.tally_me()




# grid_c1.to_bubble().illustrate_me()

# calliope.illustrate_me(bubble=block_c1)