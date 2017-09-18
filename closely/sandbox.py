import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)


class RhythmLine(calliope.Line):
    metrical_durations = ( (2,4),(2,4), ) * 6


class RhythmTest(calliope.LineBlock):
    class Line1(RhythmLine):
        phrase_i = sequences.PhraseMaker(
            rhythm_pattern = rhythms.UPBEAT_CLOCK_RHYTHM_PATTERN
            )(
                rhythm_lengths = (4,3,4,6),
                fill_rests=True,
            )

    class Line2(RhythmLine):
        phrase_i = sequences.PhraseMaker(
            rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
            )(
                rhythm_lengths = (4,3,4,6)
            )

r = RhythmTest()

print( 
    len( [l for l in r["Line1"].logical_ties if not l.rest] ), 
    len( [l for l in r["Line2"].logical_ties if not l.rest] ), 
    )

calliope.illustrate_me(bubble=RhythmTest)