import pandas as pd
import abjad
import calliope

from closely.libraries.sequences import PITCH_SEQUENCE, PitchSequence, PhraseMaker, TransformAddConstantPitch
from closely.libraries.rhythms import UPBEAT_SPACED_RHYTHM_PATTERN

pitch_sequence_1 = PitchSequence()
pitch_root_1 = "C3"


# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PHRASES:

selections_c_up = (0,1,2,2,3)
selections_c = selections_c_up + tuple(reversed(selections_c_up))

c1_phrase_maker = PhraseMaker(
    pitch_sequence = PITCH_SEQUENCE.select(*selections_c),
    rhythm_pattern = UPBEAT_SPACED_RHYTHM_PATTERN,
    )

# _____________________________________________________________________________________
# _____________________________________________________________________________________
# LineBlocks:

def hill_range_maker(start, steps, increment=1, span=12):
    hill_range = [start + increment*i for i in range(steps)]
    hill_range += reversed(hill_range)
    return [(b, b+span) for b in hill_range]


class BlockC1(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10), (0,3,7), (0,5,10), (0,4,7), ) 
    # TO DO: CONSIDER THESE INTERVALS:
    # intervals = ( (0,5,10), (0,3,8), (0,4,7), (0,5,10), ) 
    line_c = c1_phrase_maker(
        rhythm_lengths = (9,9),
        fill_rests = True
        )
    transform_add_pitch = TransformAddConstantPitch(
        pitch=-12,
        )
    transform_through_pitch_grid = calliope.PitchesThroughGrid(
        calliope.TallyCircleOfFifthsRange(over_range_multiplier=-99), 
        calliope.TallyParallelIntervals(interval_ratings=[(0,-20), (7,-11)]), 
        calliope.TallyMelodicIntervals(
                interval_ratings=[(0, -200), (1,40), (2,80), (3,60), (4,50), (5,6), (6,-20), (7,-4), (10,-30), (11,-50), (12,-4)], 
                over_incremental_multiplier=(12,-80),
                up_rating=-12,
                down_rating=20,
                ),
        calliope.TallyRepeatedJumps(),
        pitch_ranges = pd.DataFrame.from_records([
                hill_range_maker(9, 6, 2), # flute
                hill_range_maker(-4, 6, 2), # clarinet
                hill_range_maker(9, 6, -3), # viola
                hill_range_maker(-3, 6, -3), # cello
            ]),
        version = 1, # TO DO: consider whether version should be included here
        )

    def tally_pitches(self):
        self.transform_through_pitch_grid.grid.tally_loop()
        self.transform_through_pitch_grid.transform_nodes(self)


c1_a = BlockC1(name="c1_a")
# c1_a.transform_through_pitch_grid.grid.illustrate_start()
# c1_a.transform_through_pitch_grid.grid.illustrate_me()
c1_a.illustrate_me()
# print(c1_a[1][0][2][0].pitch)

# calliope.illustrate_me(bubble=c1_a)