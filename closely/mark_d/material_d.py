import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

d_star_i = phrases.star_i_a_1(name="d_star_i")
calliope.Transpose(interval=1).transform_nodes(d_star_i)

d_star_ii = phrases.star_ii_a_1(name="d_star_ii")
calliope.Transpose(interval=1).transform_nodes(d_star_ii)

# DAH CONFUSING!
class DStarIII(calliope.LineBlock):
    line_0 = phrases.StarRhythmLineBlock.Line_I()()
    line_1 = phrases.StarRhythmLineBlock.Line_I()()
    line_2 = phrases.StarRhythmLineBlock.Line_II()
    line_3 = line_2()

d_star_iii = DStarIII()

d_sequence = (d_star_i, d_star_ii, d_star_iii)

calliope.illustrate_me(bubble = d_star_iii)

# d_star_i.illustrate_me()