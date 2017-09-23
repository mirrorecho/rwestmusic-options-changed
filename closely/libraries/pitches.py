import calliope
from closely.libraries import sequences

# _______________________________________________________________________________

PITCH_CELL = (0, 2, 3, 5)

# _______________________________________________________________________________

def with_reversed(selection):
    return selection + tuple(reversed(selection))

def down(selection=(0,1)):
    return tuple([s * -1 for s in selection])

def rotate(selection, rotation):
    return tuple([selection[(i + rotation) % len(selection)] for i in range(len(selection))])

PITCH_SELECT_SKIP = (0, 2)
PITCH_SELECT_CAUTIOUS = (0, 1, 2, 1)
PITCH_SELECT_WAVER = (0, 1, 3, 2)
PITCH_SELECT_STUTTER = (0, 1, 2, 2, 3)
PITCH_SELECT_WILD = (4, 5, 0, 1, -2, 6)
PITCH_SELECT_STAR = (0, 1, 3, 4, 2, 5)

# _______________________________________________________________________________

PITCH_SEQUENCE = sequences.PitchSequence(*PITCH_CELL)
PITCH_SEQUENCE_DOWN = PITCH_SEQUENCE.select(*down())
PITCH_SEQUENCE_SKIP = PITCH_SEQUENCE.select(*PITCH_SELECT_SKIP)
PITCH_SEQUENCE_WILD = PITCH_SEQUENCE.select(*PITCH_SELECT_WILD)
PITCH_SEQUENCE_STAR = PITCH_SEQUENCE.select(*PITCH_SELECT_STAR)

# def down(pitch_sequence):
#     return pitch_sequence.select(*select_down())

# def skip():
#     pass

# def stutter():
#     pass

# def waver():
#     pass

# def cautious():
#     pass

# def with_reversed():
#     pass

# _______________________________________________________________________________

CHORDS_FOURTHS = ( (0, 5, 10), )
CHORDS_MINOR = ( (0, 3, 7), )
CHORDS_MAJOR = ( (0, 4, 7), )

CHORDS_ALT_MINOR = CHORDS_FOURTHS + CHORDS_MINOR

CHORDS_ALT_MAJOR = CHORDS_FOURTHS + CHORDS_MAJOR

CHORDS_ALT = CHORDS_ALT_MINOR + CHORDS_ALT_MAJOR

CHORDS_SEQUENCE_I = CHORDS_ALT_MINOR * 2 + CHORDS_FOURTHS
CHORDS_SEQUENCE_II = CHORDS_ALT_MAJOR * 2 + CHORDS_FOURTHS

CHORDS_SEQUENCE_STAR = CHORDS_SEQUENCE_I * 2 + CHORDS_SEQUENCE_II

