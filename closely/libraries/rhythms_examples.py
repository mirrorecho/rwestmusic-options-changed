import abjad
import calliope

from closely.libraries import sequences, rhythms

class RhythmExamples(calliope.Score):
    # stylesheets=("../../stylesheets/score.ily",)
    pass


def get_rhythm_phrases(phrase_name, lengths=(8,8)):
    rhythm_phrases = sequences.DronePhraseFactory(
        rhythm_pattern=rhythms.__dict__[phrase_name], 
        rhythm_lengths=lengths
        )
    rhythm_phrases.metrical_durations = ((2,4),) * round(rhythm_phrases.beats / 2)
    rhythm_phrases.non_rest_events[0].tag(phrase_name + " (%s) " % len(rhythm_phrases[0].non_rest_events) )
    return rhythm_phrases

def see_patterns(patterns=(), lengths=()):
    score = RhythmExamples()
    for p, l in zip(patterns, lengths):
        score[p] = calliope.RhythmicStaff(
        get_rhythm_phrases(p, l),
        name=p, 
        )
    score.illustrate_me()


def see_all(lengths=(8,8)):
    patterns = (
        "SIMPLE_RHYTHM_PATTERN",
        "SIMPLE_BROKEN_RHYTHM_PATTERN",
        # "SLOW_RHYTHM_PATTERN",
        "GLOBE_RHYTHM_PATTERN",
        "FLUTTER_RHYTHM_PATTERN",
        "BUILD_RHYTHM_PATTERN",
        "UPBEAT_SPACED_RHYTHM_PATTERN",
        "CLOCK_RHYTHM_PATTERN",
        "UPBEAT_CLOCK_RHYTHM_PATTERN",
        "FAST_RHYTHM_PATTERN",
        "UPBEAT_BOOK_RHYTHM_PATTERN"
        )
    see_patterns(
        patterns,
        (lengths,) * len(patterns)
        )

# see_all(lengths=(4,))


# COMBOS: 

#---------------------------------------------------------
# (in 4 beats): 1 4/4 bar, with 6 non-rest events
#------------------ 
# see_patterns( 
#     ("SIMPLE_RHYTHM_PATTERN", "FAST_RHYTHM_PATTERN",),
#     ((4,4), (4,4), )
#     )

#---------------------------------------------------------
# (in 6 beats): 1.5 4/4 bars with 8 non-rest events 
#------------------ 
# see_patterns( 
#     ("SIMPLE_RHYTHM_PATTERN", "CLOCK_RHYTHM_PATTERN",),
#     ((6,6), (6,6), )
#     )
# (in 6 beats): 1.5 4/4 bars with 6 non-rest events 
#------------------ 
# see_patterns( 
#     ("GLOBE_RHYTHM_PATTERN", "UPBEAT_BOOK_RHYTHM_PATTERN", "UPBEAT_CLOCK_RHYTHM_PATTERN"),
#     ((6,6), (6,6), (6,6) )
#     )

#---------------------------------------------------------
# (in 8 beats): 2 4/4 bars, with 12 non-rest events... offsets 1/8 and 1/4 notes
#------------------ 
# see_patterns( 
#     ("CLOCK_RHYTHM_PATTERN", "BUILD_RHYTHM_PATTERN"),
#     ((8,8), (8,8) )
#     )
# (in 8 beats): 2 4/4 bars, with 8 non-rest events
#------------------ 
see_patterns( 
    ("SIMPLE_BROKEN_RHYTHM_PATTERN", "UPBEAT_BOOK_RHYTHM_PATTERN"),
    ((8,8), (8,8) )
    )

# (in 8 beats)
# - CLOCK / BUILD (2 4/4 bars, with 12 non-rest events... offsets 1/8 and 1/4 notes)
# - SIMPLE BROKEN / UPBEAT BOOK (2 4/4 bars, with 8 non-rest events)







