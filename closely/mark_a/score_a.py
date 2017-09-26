import abjad
import calliope
from closely.libraries.sequences import PhraseMaker, PitchSequence, PITCH_SEQUENCE
from closely.libraries.rhythms import (
    DRONE_RHYTHM_PATTERN, DRILL_RHYTHM_PATTERN, FLIT_RHYTHM_PATTERN)
from closely.scores import score_staves


# -----------------------------------------------------------------
# PHRASES:

flit_sequence = PITCH_SEQUENCE.select(0, 3, 4, 5, 7, 0, -1)


class FastPhraseMaker(PhraseMaker):
    pitch_sequence = flit_sequence
    rhythm_pattern = FLIT_RHYTHM_PATTERN

# TEST = FastPhraseMaker()(24,16)

# -----------------------------------------------------------------
# PARTS:


class Flute(calliope.Line): # NOTE: could also be a line...
    metrical_durations = (
        (1,4),(1,4),(1,4),(1,4),
        (4,4),
        (4,4),
        (2,4),(1,4),(1,4),
        (1,4),(1,4),(2,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        )

    phrase_0 = FastPhraseMaker(
        pitch_sequence=flit_sequence.select(0,2, keep_in_range=(12,24)),
        )(30, 3, bookend_rests=(1,))
    phrase_1 = FastPhraseMaker(
        pitch_sequence=flit_sequence(keep_in_range=(12,24)),
        )(4,20,8, bookend_rests=(32,))
    phrase_2 = FastPhraseMaker(
        pitch_sequence=flit_sequence(keep_in_range=(12,24)),
        )(4,4, 9)
    phrase_3 = FastPhraseMaker(
        pitch_sequence=flit_sequence(keep_in_range=(12,24)),
        )(6,6,)

    bracket_cells = calliope.BracketCells()
    # tagging = calliope.Tagging({
    #     (0,0,0):"[",
    #     # (0,0,2):"]",
    #     (0,0,2,0):"]",
    #     # (0,2): "]"
    #     })

f = Flute()
print(f.ly())
print(f["phrase_0"][0][1].tags)


class Clarinet(calliope.Line): # NOTE: could also be a line...
    metrical_durations = (
        (4,4),
        (4,4),
        (4,4),
        (2,4),(1,4),(1,4),
        (1,4),(1,4),(2,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        (1,4),(1,4),(1,4),(1,4),
        )
    phrase_0 = FastPhraseMaker()(4, bookend_rests=(15.5,))
    phrase_1 = FastPhraseMaker()(19, 4, bookend_rests=(22.5,) )
    phrase_2 = FastPhraseMaker()(20, 8,)
    phrase_3 = FastPhraseMaker()(4,2,2, 9)
    phrase_4 = FastPhraseMaker()(3,3,2,4)
    # phrase_1 = FastPhraseMaker(
    #     pitch_sequence=flit_sequence(transpose=-5, keep_in_range=(5,18)),
    #     )(24,16)
    # phrase_2 = FastPhraseMaker(
    #     pitch_sequence=flit_sequence(transpose=-2, keep_in_range=(5,18)),
    #     )(24,16)
    # phrase_3 = FastPhraseMaker(
    #     pitch_sequence=flit_sequence(keep_in_range=(9,21)),
    #     )(12,)
    # phrase_4 = FastPhraseMaker(
    #     pitch_sequence=flit_sequence.select(-1,0, keep_in_range=(14,26)),
    #     )(8,4)

    bracket_cells = calliope.BracketCells()

class Violin(calliope.Line): 
    metrical_durations = (
        (1,4),(1,4),(2,4),
        (4,4),
        (4,4),
        (2,4),(1,4),(1,4),
        (1,4),(1,4),(2,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        (4,4),
        )

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

    bracket_cells = calliope.BracketCells()


class Cello(calliope.Segment): # NOTE: could also be a line...
    music_contents= "c'1"

print(Violin().beats)

calliope.illustrate_me(score_type=score_staves.CloselyScore)