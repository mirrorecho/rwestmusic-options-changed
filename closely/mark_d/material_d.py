import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

d_star_i = phrases.star_i_a_1(name="d_star_i")
calliope.Transpose(interval=1).transform_nodes(d_star_i)

d_star_ii = phrases.star_ii_a_1(name="d_star_ii")
calliope.Transpose(interval=1).transform_nodes(d_star_ii)

class DStarIII(calliope.PhraseBlock):
    class PhraseFlute(phrases.StarRhythmPhrase): pass
    class PhraseClarinet(phrases.StarRhythmPhrase): pass
    class PhraseViolin(phrases.SubRhythmPhrase): pass
    class PhraseCello(phrases.SubRhythmPhrase): pass

class DStarIV(calliope.PhraseBlock):
    class PhraseFlute(phrases.StarRhythmPhrase): pass
    class PhraseClarinet(phrases.StarRhythmPhrase): pass
    class PhraseViolin(phrases.SubRhythmPhrase): pass
    class PhraseCello(phrases.SubRhythmPhrase): pass

d_star_iii = DStarIII(name="d_star_iii")

d_star_iv = DStarIV(name="d_star_iv")

d_star_v = d_star_ii(name="d_star_v")

d_sequence = (
    d_star_i, 
    d_star_ii, 
    d_star_iii,
    d_star_iv,
    d_star_v,
    )

# calliope.illustrate_me(bubble = d_star_iii)
# d_star_i.illustrate_me()