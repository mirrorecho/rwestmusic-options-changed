import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers)


class StarRhythmPhrase(PhraseFactory):
    rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN
    rhythm_lengths = (10,8)
    fill_rests=True
    pitch_sequence = sequences.PitchSequence(0,0)

StarRhythmPhrase().illustrate_me()





# class RhythmLine(calliope.Line):
#     metrical_durations = ( (2,4),(2,4), ) * 6

# class MyTransform(calliope.Transform):
#     def transform_nodes(self, machine):
#         for c in machine.cells:
#             c[0].fuse(1)
#             c[2].fuse(1)
#             c[4].fuse(1)
#         machine.events[-2].fuse(1)
#         machine.remove_empty()
#         machine.cells[1].append(calliope.RestEvent(2))



# class RhythmTest(calliope.LineBlock):
#     class Line1(RhythmLine):
#         phrase_i = sequences.PhraseMaker(
#             rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN
#             )(
#                 rhythm_lengths = (10,8),
#                 fill_rests=True,
#             )

#     class Line2(RhythmLine):
#         phrase_i = sequences.PhraseMaker(
#             rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
#             )(
#                 rhythm_lengths = (4,4,6), 
#                 bookend_rests = (2,)
#             )

#         yo_ha = MyTransform()

#         # class InsertPause(calliope.Transform):
#         #     def transform_nodes(self, machine):
#         #         print(machine)
#         #         machine.cells[1].append(calliope.RestEvent(1))

#     brackets = calliope.BracketByType(by_type=calliope.Event)

# r = RhythmTest()
# r2 = RhythmTest()

# print( r["Line1"].rhythm  )

# r["Line1"].rhythm = (1,) * len(r["Line1"].logical_ties)


print( 
    len( r["Line1"].non_rest_events ), 
    len( r["Line2"].non_rest_events ), 
    )

calliope.illustrate_me(bubble=r)