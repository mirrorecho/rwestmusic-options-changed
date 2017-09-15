import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import DRONE_RHYTHM_PATTERN, DRILL_RHYTHM_PATTERN, UPBEAT_CLOCK_RHYTHM_PATTERN


# -----------------------------------------------------------------
# PHRASES:

class ClockPhrase(PhraseMaker):
    # pitch_sequence = PitchSequence(-8, -8)
    rhythm_pattern = UPBEAT_CLOCK_RHYTHM_PATTERN


class LineA(calliope.Line): 
    phrase_0 = ClockPhrase()(6, 6)
    phrase_1 = ClockPhrase()(6, 6, fill_rests=True)

calliope.illustrate_me()