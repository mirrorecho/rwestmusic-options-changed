import abjad
import calliope

from closely.libraries.sequences import PITCH_SEQUENCE, PitchSequence, PhraseMaker, TransformAddConstantPitch
from closely.libraries.rhythms import UPBEAT_SPACED_RHYTHM_PATTERN, FAST_RHYTHM_PATTERN
from closely.libraries.pitch_ranges import hill_ranges_maker
from closely.libraries.tally_apps import LINE_TALLY_APPS

pitch_sequence_1 = PitchSequence()
pitch_root_1 = "C3"


# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PHRASES:

selections_c_up = (0,1,2,2,3)
selections_c = selections_c_up + tuple(reversed(selections_c_up))

selections_c_down = (0,-1,-3, -2)
selections_c_down_more = (0,-1,)

c_phrase_maker = PhraseMaker(
    pitch_sequence = PITCH_SEQUENCE.select(*selections_c),
    rhythm_pattern = UPBEAT_SPACED_RHYTHM_PATTERN,
    )

c_fast_phrase_maker = PhraseMaker(
    pitch_sequence = PITCH_SEQUENCE.select(*selections_c[:7]),
    rhythm_pattern = FAST_RHYTHM_PATTERN,
    )

# _____________________________________________________________________________________
# _____________________________________________________________________________________
# LineBlocks:

class BlockC(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = ( (0,5,10), (0,3,7), (0,5,10), (0,4,7), ) 
    # TO DO: CONSIDER THESE INTERVALS:
    # intervals = ( (0,5,10), (0,3,8), (0,4,7), (0,5,10), ) 
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = 0

    class PitchesThroughGrid(calliope.PitchesThroughGrid):
        tally_apps = LINE_TALLY_APPS
        pitch_ranges = hill_ranges_maker(6)
        version = 1

    # transform_add_pitch = TransformAddConstantPitch(pitch=0)
    # transform_through_pitch_grid = calliope.PitchesThroughGrid(
    #     *LINE_TALLY_APPS,
    #     pitch_ranges = hill_ranges_maker(6),
    #     version = 1, # TO DO: consider whether version should be included here
    #     )
    def tally_pitches(self):
        self.pitch_grid.tally_loop()
        self.transforms_tree["PitchesThroughGrid"].transform_nodes(self)

class BlockC_I(BlockC):
    line_c = c_phrase_maker(
        rhythm_lengths = (9,9),
        bookend_rests = (4,),
        fill_rests = True
        )

class BlockC_II(BlockC_I):
    line_c = c_phrase_maker(
        rhythm_lengths = (13,),
        bookend_rests = (6,),
        fill_rests = True
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = -2

class BlockC_III(BlockC_II):
    intervals = ( (0,5,10), )
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (4,3),
        bookend_rests = (3,),
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = -2

class BlockC_IV(BlockC_III):
    intervals = BlockC.intervals
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (3,3,3),
        pitch_sequence_index = 7,
        bookend_rests = (1,),
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = 0

class BlockC_V(BlockC_IV):
    intervals = ( (0,5,10), (0,4,7), ) 
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (3,2,2),
        pitch_sequence = PITCH_SEQUENCE.select(*selections_c_down),
        bookend_rests = (3,),
        )

class BlockC_VI(BlockC_V):
    # TO DO... the ONLY thing that's different here is the bookend rest
    # consider DRY
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (3,2,2),
        pitch_sequence = PITCH_SEQUENCE.select(*selections_c_down),
        bookend_rests = (1,),
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = 2

class BlockC_VII(BlockC):
    # TO DO... the ONLY thing that's different here is the bookend rest
    # consider DRY
    intervals = ( (0,5,10), )
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (8,),
        pitch_sequence = PITCH_SEQUENCE.select(*selections_c_down),
        bookend_rests = (1,),
        pitch_sequence_index = 1,
        transpose=12,
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = 4

class BlockC_VIII(BlockC_VII):
    line_c = c_fast_phrase_maker(
        rhythm_lengths = (10,),
        pitch_sequence = PITCH_SEQUENCE.select(*selections_c_down_more),
        pitch_sequence_index = -3,
        transpose=12,
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = 6

class BlockC_IX(BlockC):
    intervals = ( (0,4,7), )
    line_c = PhraseMaker()(
        rhythm_lengths = (9,),
        pitch_sequence = PITCH_SEQUENCE.select(*selections_c_down_more),
        pitch_sequence_index = 3,
        transpose=12,
        )
    class AddConstantPitch(TransformAddConstantPitch):
        pitch = -1


c_i = BlockC_I(name="c_i")
c_ii = BlockC_II(name="c_ii")
c_iii = BlockC_III(name="c_iii")
c_iv = BlockC_IV(name="c_iv")
c_v = BlockC_V(name="c_v")
c_vi = BlockC_VI(name="c_vi")
c_vii = BlockC_VII(name="c_vii")
c_viii = BlockC_VIII(name="c_viii")
c_ix = BlockC_IX(name="c_ix")
c_x = c_ix(name="c_x")

c_sequence = (c_i, c_ii, c_iii, c_iv, c_v, c_vi, c_vii, c_viii, c_ix, c_x)

# c_i.transform_through_pitch_grid.grid.illustrate_start()
# c_i.transform_through_pitch_grid.grid.illustrate_me()
# c_ix.illustrate_me()


