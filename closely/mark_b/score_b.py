import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import SLOW_RHYTHM_PATTERN, SIMPLE_BROKEN_RHYTHM_PATTERN

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely import score_staves

# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PHRASES

pitch_sequence_b1 = PITCH_SEQUENCE.select(0,3,2,1,4,1)

fast_phrase_maker = PhraseMaker(
    rhythm_pattern = SIMPLE_BROKEN_RHYTHM_PATTERN,
    pitch_sequence = pitch_sequence_b1,
    )


# _____________________________________________________________________________________
# _____________________________________________________________________________________
# PARTS

class MarkB(calliope.LineBlock):
    class Flute(calliope.Line): 
        phrase_0 = fast_phrase_maker(
            rhythm_lengths=(4,4,4)
            )

    class Clarinet(calliope.Line): 
        phrase_0 = fast_phrase_maker(
            rhythm_lengths=(4,4,4)
            )

    class Violin(calliope.Line): 
        phrase_0 = fast_phrase_maker(
            rhythm_lengths=(4,4,4)
            )

    class Cello(calliope.Line): 
        phrase_0 = fast_phrase_maker(
            rhythm_lengths=(4,4,4)
            )


# _____________________________________________________________________________________
# _____________________________________________________________________________________

mark_b_bubble = MarkB()

# calliope.SmartRange(-24,-2).transform_nodes(mark_b_bubble["Cello"])

calliope.illustrate_me(bubble=mark_b_bubble, score_type=score_staves.CloselyScore)