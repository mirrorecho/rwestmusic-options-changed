import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import SLOW_RHYTHM_PATTERN, SIMPLE_BROKEN_RHYTHM_PATTERN

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely import score_staves


# -----------------------------------------------------------------
# TO CONSIDER... MOVE ALL OF THIS TO C AND C TO D????????


# -----------------------------------------------------------------
# PHRASES:

# pitch_sequence_skips_waver-1
pitch_sequence_0 = PITCH_SEQUENCE.select(4, 5, 0, 1, -2, 6, transpose=-3)
pitch_sequence_0_alt = pitch_sequence_0.select(1,3)
pitch_sequence_0_alt2 = pitch_sequence_0.select(0,2)

slow_drone_maker = PhraseMaker(
    rhythm_pattern = SLOW_RHYTHM_PATTERN,
    )
fast_drone_maker = PhraseMaker(
    rhythm_pattern = SIMPLE_BROKEN_RHYTHM_PATTERN,
    )
slow_phrase_maker = PhraseMaker(
    rhythm_pattern = SLOW_RHYTHM_PATTERN,
    pitch_sequence = pitch_sequence_0,
    )
fast_phrase_maker = PhraseMaker(
    rhythm_pattern = SIMPLE_BROKEN_RHYTHM_PATTERN,
    pitch_sequence = pitch_sequence_0,
    )

# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PARTS:

class Flute(calliope.Line): 
    phrase_0 = slow_phrase_maker(
        rhythm_lengths = (6,3,3,3),
        bookend_rests = (8,4),
        pitch_sequence = pitch_sequence_0.select(0,2),
        )
    phrase_1 = fast_phrase_maker(
        rhythm_lengths = (6,4,4,2,4,2,4,4,2),
        bookend_rests = (12,),
        pitch_sequence = pitch_sequence_0.select(-3, -1).select(0,1,2,1),
        )
    tagging = calliope.Tagging({
        0:("pp",)
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(4,32)
# ___________________________________________________________
class Clarinet(calliope.Line): 
    phrase_0 = slow_phrase_maker(
        rhythm_lengths = (6,6),
        bookend_rests=(8,4),
        )
    phrase_1 = fast_phrase_maker( # NOTE... almost the same as Flute phrase_1... DRY?
        rhythm_lengths = (6,4,4,2,4,2,4,4,2),
        bookend_rests = (12,),
        pitch_sequence = pitch_sequence_0.select(-2, 0).select(0,1,2,1),
        )
    tagging = calliope.Tagging({
        0:("pp",)
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(-3,24)
# ___________________________________________________________
class Violin(calliope.Line): 
    phrase_0 = slow_phrase_maker(
        rhythm_lengths = (6,3,3,3),
        bookend_rests = (8,4),
        pitch_sequence = pitch_sequence_0.select(1,3),
        )
    phrase_1 = fast_phrase_maker(
        rhythm_lengths = (6,4,8,6,4,4,),
        bookend_rests = (12,),
        pitch_sequence = pitch_sequence_0.select(-1,0),
        )
    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(-5,20)
# ___________________________________________________________
class Cello(calliope.Line): 
    phrase_0 = slow_drone_maker(
        transpose = -8,
        rhythm_lengths = (8,8),
        )
    phrase_1 = fast_drone_maker(
        transpose = -8,
        rhythm_lengths = (8,6,4)
        )
    phrase_2 = fast_drone_maker(
        transpose = -3,
        rhythm_lengths = (8,6,4,4)
        )
    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        (1, -1):"\<",
        2:"mp"
        })
    bracket_cells = calliope.BracketCells()

# print(Cello().beats)

# s = CloselyScore()
# print(s[0].ly())

calliope.illustrate_me(score_type=score_staves.CloselyScore)


