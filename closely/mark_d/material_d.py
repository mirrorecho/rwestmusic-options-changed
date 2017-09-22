import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

d_star_i = phrases.star_i_a_1(name="d_star_i")
calliope.Transpose(interval=1).transform_nodes(d_star_i)

d_star_ii = phrases.star_ii_a_1(name="d_star_ii")
calliope.Transpose(interval=1).transform_nodes(d_star_ii)

class DStarIII(calliope.LineBlock):
    class Line0(calliope.Line):
        phrase_i = phrases.StarRhythmPhrase()

    class Line1(calliope.Line):
        phrase_i = phrases.StarRhythmPhrase()

    class Line2(calliope.Line):
        phrase_i = phrases.SubRhythmPhrase()

    class Line3(calliope.Line):
        phrase_i = phrases.SubRhythmPhrase()

d_star_iii = DStarIII(name="d_star_iii")

d_sequence = (
    # d_star_i, 
    # d_star_ii, 
    d_star_iii,
    )

# calliope.illustrate_me(bubble = d_star_iii)
# d_star_i.illustrate_me()