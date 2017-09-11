import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import (
    DRONE_RHYTHM_PATTERN, DRILL_RHYTHM_PATTERN, FLIT_RHYTHM_PATTERN)

# -----------------------------------------------------------------
# PHRASES:

flit_sequence = PITCH_SEQUENCE.select(0, 3, 4, 5, 7, 0, -1)


class FastPhraseMaker(PhraseMaker):
    pitch_sequence = flit_sequence
    rhythm_pattern = FLIT_RHYTHM_PATTERN

# TEST = FastPhraseMaker()(24,16)

# -----------------------------------------------------------------
# PARTS:


class Flute(calliope.Segment): # NOTE: could also be a line...
    music_contents= "c'1"

class Clarinet(calliope.Segment): # NOTE: could also be a line...
    music_contents= "c'1"

class Violin(calliope.Line): 
    phrase_0 = FastPhraseMaker()(32,24)
    phrase_1 = FastPhraseMaker(
        pitch_sequence=flit_sequence(transpose=-5, keep_in_range=(5,18)),
        )(24,16)
    phrase_2 = FastPhraseMaker(
        pitch_sequence=flit_sequence(transpose=-2, keep_in_range=(5,18)),
        )(24,16)
    phrase_3 = FastPhraseMaker(
        pitch_sequence=flit_sequence(keep_in_range=(9,21)),
        )(12,)
    phrase_4 = FastPhraseMaker(
        pitch_sequence=flit_sequence.select(-1,0, keep_in_range=(14,26)),
        )(8,4)

class Cello(calliope.Segment): # NOTE: could also be a line...
    music_contents= "c'1"

print(Violin().beats)

calliope.illustrate_me()