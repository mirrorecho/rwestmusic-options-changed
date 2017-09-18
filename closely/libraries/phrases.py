import abjad
import calliope
from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers)


star_phrase_maker_i = sequences.PhraseMaker(
    pitch_sequence = pitches.PITCH_SEQUENCE_STAR,
    rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN,
    )

star_phrase_maker_ii = sequences.PhraseMaker(
    pitch_sequence = pitches.PITCH_SEQUENCE_STAR,
    rhythm_pattern = rhythms.CLOCK_RHYTHM_PATTERN,
    )

star_phrase_maker_iii = sequences.PhraseMaker(
    pitch_sequence = pitches.PITCH_SEQUENCE_STAR,
    rhythm_pattern = rhythms.UPBEAT_CLOCK_RHYTHM_PATTERN,
    )
# _______________________________________________________________________________

class StarPhraseBlock(calliope.LineStacked):
    # TO DO: should not have to specify child_types here...
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = pitches.CHORDS_SEQUENCE_STAR
    class AddConstantPitch(sequences.TransformAddConstantPitch):
        pitch = -2

class StarPhraseBlock_I(StarPhraseBlock):
    star_line = star_phrase_maker_i(
        rhythm_lengths = (10,8),
        fill_rests = True,
        )

class StarPhraseBlock_II(StarPhraseBlock):
    # TO CONSIDER... always apply rotation to intervals equivalent to pitch_sequence_index??
    intervals = pitches.rotate(pitches.CHORDS_SEQUENCE_STAR, -5)
    star_line = star_phrase_maker_ii(
        rhythm_lengths = (5,7),
        fill_rests = True,
        pitch_sequence_index = -5,
        )

class StarPhraseBlock_III(StarPhraseBlock):
    intervals = pitches.rotate(pitches.CHORDS_SEQUENCE_STAR, 6)
    star_line = star_phrase_maker_iii(
        rhythm_lengths = (5,5),
        fill_rests = True,
        pitch_sequence_index = 6,
        transpose=-12
        )
# _______________________________________________________________________________

class StarGridMixin(StarPhraseBlock):
    class PitchesThroughGrid(calliope.PitchesThroughGrid):
        tally_apps = tally_apps_lib.LINE_SMOOTH_TALLY_APPS
        pitch_ranges = pitch_range_helpers.mid_ranges_maker()
    def tally_pitches(self):
        self.pitch_grid.tally_loop()
        self.transforms_tree["PitchesThroughGrid"].transform_nodes(self)

class StarPhraseBlock_I_Grid_A(StarPhraseBlock_I, StarGridMixin): pass
class StarPhraseBlock_II_Grid_A(StarPhraseBlock_II, StarGridMixin): pass
class StarPhraseBlock_III_Grid_A(StarPhraseBlock_II, StarGridMixin): pass

# TO DO: figure out versioning
star_i_a_1 = StarPhraseBlock_I_Grid_A(name="star_i_a")
star_ii_a_1 = StarPhraseBlock_II_Grid_A(name="star_ii_a")

# ============================================================


# calliope.illustrate_me(bubble=star_i_a_1)