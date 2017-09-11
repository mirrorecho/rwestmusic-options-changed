import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import DRONE_RHYTHM_PATTERN, DRILL_RHYTHM_PATTERN

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely import score_staves


# -----------------------------------------------------------------
# TO CONSIDER... MOVE ALL OF THIS TO C AND C TO D????????


# -----------------------------------------------------------------
# PHRASES:

class DronePhrase(PhraseMaker):
    pitch_sequence = PitchSequence(-8, -8)
    rhythm_pattern = DRONE_RHYTHM_PATTERN

class DroneFast(DronePhrase):
    rhythm_pattern = DRILL_RHYTHM_PATTERN

pitch_sequence_a = PITCH_SEQUENCE.select(4, 5, 0, 1, -2, 6, transpose=-3)
# pitch_sequence_b = pitch_sequence_a.select(1,3)

class PitchedPhrase(DronePhrase):
    pitch_sequence = pitch_sequence_a

class PitchedPhraseFast(DronePhrase):
    pitch_sequence = pitch_sequence_a
    rhythm_pattern = DRILL_RHYTHM_PATTERN


# -----------------------------------------------------------------
# PARTS:

class Flute(calliope.Line): 

    phrase_0 = PitchedPhrase(
        pitch_sequence = pitch_sequence_a.select(0,2)(keep_in_range=(12, 29))
        )(6, 6, bookend_rests=(8,4))
    
    phrase_1 = PitchedPhraseFast(
        pitch_sequence = pitch_sequence_a.select(-3, -1).select(0,1,2,1)(keep_in_range=(12, 29))
        )(6,4,4,2,4,2,4,4,2, bookend_rests=(12,))

    tagging = calliope.Tagging({
        0:("pp",)
        })

class Clarinet(calliope.Line): 
    phrase_0 = PitchedPhrase()(6, 6, bookend_rests=(8,4))

    phrase_1 = PitchedPhraseFast(
        pitch_sequence = pitch_sequence_a.select(-2, 0).select(0,1,2,1)(keep_in_range=(-6, 24))
        )(6,4,4,2,4,2,4,4,2, bookend_rests=(12,))
    
    tagging = calliope.Tagging({
        0:("pp",)
        })

class Violin(calliope.Line): 
    phrase_0 = PitchedPhrase(
        pitch_sequence = pitch_sequence_a.select(1,3)(keep_in_range=(-5,10))
        )(6, 6, bookend_rests=(8,4))

    phrase_1 = PitchedPhraseFast(
        pitch_sequence = pitch_sequence_a.select(-1,0)(keep_in_range=(-5,24))
        )(6,4,8,6,4,4, bookend_rests=(12,))

    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        })

class Cello(calliope.Line): 
    phrase_0 = DronePhrase()(8)
    phrase_1 = DronePhrase()(8)
    phrase_2 = DroneFast()(8,6,4)
    phrase_3 = DroneFast(pitch_sequence=PitchSequence(-3, -3))(8,6,4,4)

    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        (2, -1):"\<",
        3:"mp"
        })

# print(Cello().beats)

# s = CloselyScore()
# print(s[0].ly())

calliope.illustrate_me(score_type=score_staves.CloselyScore)


