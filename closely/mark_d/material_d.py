import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

class DStarI(phrases.GridMask, phrases.StarPhraseBlock_I_Grid_A):
    # TO DO... RE-ENABLE BELOW (ONLY DISABLED FOR TESTING PURPOSES WITH SELECTION)
    pass
    # transpose_up = calliope.Transpose(interval=1)
    # pitches_from_grid_bubble = phrases.star_i_a_1
    # def set_children_from_class(self, *args, **kwargs):
    #     super().set_children_from_class(*args, **kwargs)
    #     for phrase_line in self:
    #         # phrase_line.first_non_rest.tag(">")
    #         phrase_line.respell = "sharps"

class DStarII(phrases.GridMask, phrases.StarPhraseBlock_II_Grid_A):
    transpose_up = calliope.Transpose(interval=1)
    pitches_from_grid_bubble = phrases.star_ii_a_1
    def set_children_from_class(self, *args, **kwargs):
        super().set_children_from_class(*args, **kwargs)
        for phrase_line in self:
            # phrase_line.first_non_rest.tag(">")
            phrase_line.respell = "sharps"
            phrase_line.add_bookend_rests(8,4)

class DStarIII(calliope.PhraseBlock):
    class PhraseFlute(phrases.StarRhythmPhrase): 
        pitch_sequence = pitches.PITCH_SEQUENCE_CAUTIOUS
        transpose = 16
    class PhraseClarinet(phrases.StarRhythmPhrase):
        pitch_sequence = pitches.PITCH_SEQUENCE_CAUTIOUS
        pitch_sequence_index = 1
        transpose = 4
    class PhraseViolin(phrases.SubRhythmPhrase): 
        pitch_sequence = pitches.PITCH_SEQUENCE_WAVER
        transpose = -1
        pitch_sequence_index = 3
    class PhraseCello(phrases.SubRhythmPhrase): 
        pitch_sequence = pitches.PITCH_SEQUENCE_WAVER
        transpose = -8
        pitch_sequence_index = -4

class DStarIV(DStarIII):
    class PhraseFlute(DStarIII.PhraseFlute): 
        pitch_sequence_index = DStarIII.PhraseFlute.pitch_sequence_index + 5
    class PhraseClarinet(DStarIII.PhraseClarinet): 
        pitch_sequence_index = DStarIII.PhraseClarinet.pitch_sequence_index + 5
    class PhraseViolin(DStarIII.PhraseViolin): 
        pitch_sequence_index = DStarIII.PhraseViolin.pitch_sequence_index + 5
    class PhraseCello(DStarIII.PhraseCello): 
        pitch_sequence_index = DStarIII.PhraseCello.pitch_sequence_index + 5

class DStarV(DStarII):
    # V is almost the same as II...
    transpose_up = calliope.Transpose(interval=2)
    def set_children_from_class(self, *args, **kwargs):
        phrases.StarPhraseBlock_II_Grid_A.set_children_from_class(self, *args, **kwargs)
        for phrase_line in self:
            # phrase_line.first_non_rest.tag(">")
            phrase_line.respell = "flats"
            # phrase_line.add_bookend_rests(8)


class DStarVI(phrases.GridMask, phrases.StarPhraseBlock_III_Grid_A):
    transpose_up = calliope.Transpose(interval=2)
    pitches_from_grid_bubble = phrases.star_iii_a_1
    def set_children_from_class(self, *args, **kwargs):
        super().set_children_from_class(*args, **kwargs)
        for phrase_line in self:
            phrase_line.respell = "flats"
            # phrase_line.add_bookend_rests(2)

class DStarVII(DStarVI):
    transpose_up = calliope.Transpose(interval=-3)

class DStarVIII(DStarVII):
        transpose_up = calliope.Transpose(interval=4)

d_star_i = DStarI(name="d_star_i")

d_star_ii = DStarII(name="d_star_ii")

d_star_iii = DStarIII(name="d_star_iii")

d_star_iv = DStarIV(name="d_star_iv")

d_star_v = DStarV(name="d_star_v")

d_star_vi = DStarVI(name="d_star_vi")

d_star_vii = DStarVII(name="d_star_vii")

d_star_viii = DStarVIII(name="d_star_viii")

d_sequence = (
    d_star_i, 
    d_star_ii, 
    d_star_iii,
    d_star_iv,
    d_star_v,
    d_star_vi,
    d_star_vii,
    d_star_viii,
    )

# calliope.illustrate_me(bubble = d_star_iv)