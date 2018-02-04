import abjad
import calliope
from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely.scores import score_staves


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
    
# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PARTS:

class Flute(calliope.Line): 

    class Phrase0_I(SlowPhrase0):
        rhythm_lengths = (6,3,3,3)
        bookend_rests = (8,4)
        pitch_selections = (0,2)

    class Phrase0_II(FastPhrase0):
        rhythm_lengths = (6,4,4,2,4,2,4,4,2)
        bookend_rests = (12,)
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-3, -1).select(0,1,2,1)

    tagging = calliope.Tagging({
        0:("pp",)
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(4,32)
# ___________________________________________________________

class Clarinet(calliope.Line): 

    class Phrase0_I(SlowPhrase0):
        rhythm_lengths = (6,6)
        bookend_rests=(8,4)

    class Phrase0_II(Flute.Phrase0_II):
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-2, 0).select(0,1,2,1)

    tagging = calliope.Tagging({
        0:("pp",)
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(-3,24)
# ___________________________________________________________

class Violin(calliope.Line): 

    class Phrase0_I(Flute.Phrase0_I):
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(1,3)

    class Phrase0_II(FastPhrase0):
        rhythm_lengths = (6,4,8,6,4,4,)
        bookend_rests = (12,)
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-1,0)

    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(-5,20)
# ___________________________________________________________

class Cello(calliope.Line): 
    
    class Phrase0_I(SlowRhythm):
        transpose = -8
        rhythm_lengths = (8,8)

    class Phrase0_II(FasterRhythm):
        transpose = -8
        rhythm_lengths = (8,6,4)

    class Phrase0_III(FasterRhythm):
        transpose = -3
        rhythm_lengths = (8,6,4,4)

    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        (1, -1):"\<",
        2:"mp"
        })
    bracket_cells = calliope.BracketCells()

# print(Cello().beats)

# c.illustrate_me()
# print(s[0].ly())

calliope.illustrate_me(score_type=score_staves.CloselyScore, as_midi=True)


