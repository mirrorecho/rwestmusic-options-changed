import abjad
import calliope
from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely.scores import score_staves
from closely.mark_0 import material_0


    
# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PARTS:

# class Violin1(calliope.Line): 

#     class Phrase0_I(material_0.Phrase0_I):
#         pitch_selections = (0,2)

#     class Phrase0_II(material_0.Phrase0_II):
#         pass

#     tagging = calliope.Tagging({
#         0:("pp",)
#         })
#     bracket_cells = calliope.BracketCells()
#     my_range = calliope.SmartRange(4,32)
# # ___________________________________________________________

# class Violin2(calliope.Line): 

#     class Phrase0_I(material_0.Phrase0_I):
#         rhythm_lengths = (6,6)

#     class Phrase0_II(material_0.Phrase0_II):
#         pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-2, 0).select(0,1,2,1)

#     tagging = calliope.Tagging({
#         0:("pp",)
#         })
#     bracket_cells = calliope.BracketCells()
#     my_range = calliope.SmartRange(-3,24)
# # ___________________________________________________________

class Viola(calliope.Line): 

    class Phrase0_I(material_0.Phrase0_I):
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(1,3)

    class Phrase0_II(material_0.Phrase0_II):
        rhythm_lengths = (6,4,8,6,4,4,)
        pitch_sequence = pitches.PITCH_SEQUENCE_WILD.select(-1,0)

    tagging = calliope.Tagging({
        0:("pp", "sul. pont"),
        })
    bracket_cells = calliope.BracketCells()
    my_range = calliope.SmartRange(-5,20)
# ___________________________________________________________

# class Cello(calliope.Line): 
    
#     class Phrase0_I(material_0.SlowRhythm):
#         transpose = -8
#         rhythm_lengths = (8,8)

#     class Phrase0_II(material_0.FasterRhythm):
#         transpose = -8
#         rhythm_lengths = (8,6,4)

#     class Phrase0_III(material_0.FasterRhythm):
#         transpose = -3
#         rhythm_lengths = (8,6,4,4)

#     tagging = calliope.Tagging({
#         0:("pp", "sul. pont"),
#         (1, -1):"\<",
#         2:"mp"
#         })
#     bracket_cells = calliope.BracketCells()

# def transform(score):
#     for part in score:
#         part.events[0].tag("pp")



# print(Cello().beats)

# c.illustrate_me()
# print(s[0].ly())

calliope.illustrate_me(score_type=score_staves.CloselyScore, as_midi=True)


