import abjad
import calliope
from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

# -----------------------------------------------------------------
# TO CONSIDER... MOVE ALL OF THIS TO C AND C TO D????????

# -----------------------------------------------------------------
# PHRASES:

class Phrase0PitchesMixin(object):
    pitch_sequence = pitches.PITCH_SEQUENCE_WILD
    transpose = -3

class SlowRhythm(sequences.DronePhraseFactory):
    rhythm_pattern = rhythms.SLOW_RHYTHM_PATTERN

class FasterRhythm(sequences.DronePhraseFactory):
    rhythm_pattern = rhythms.SIMPLE_BROKEN_RHYTHM_PATTERN

class SlowPhrase0(Phrase0PitchesMixin, SlowRhythm): pass

class FastPhrase0(Phrase0PitchesMixin, FasterRhythm): pass

class Phrase0_I(SlowPhrase0):
    rhythm_lengths = (6,3,3,3)
    bookend_rests = (8,4)

class Phrase0_II(FastPhrase0):
    rhythm_lengths = (6,4,4,2,4,2,4,4,2)
    bookend_rests = (12,)
    pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-3, -1).select(0,1,2,1)

    



calliope.illustrate_me()
