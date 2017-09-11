import abjad
import calliope

pitches = (1,2,3,4)
rhythm = (1,-1, -1, 1,-2,2,-1,3,4,-4,2,-4,1)

c = calliope.Cell(pitches=pitches, rhythm=rhythm, pitches_skip_rests=True)
c.illustrate_me()

# phrase_up_I.illustrate_me()




# PITCH_SEQUENCE_I = PitchSequence(*PITCH_CELL) * 5
#
# print(PITCH_SEQUENCE_I)

# class SequenceUp(caliope.Phrase):
#     class CellA(calliope.Cell):
#         class Event1(calliope.Event):
#             pitch = 0
#         class Event1(calliope.Event):
#             pitch = 0
#         class Event1(calliope.Event):
#             pitch = 0
#     class CellB(calliope.Cell):
#     class CellC(calliope.Cell):


# calliope.illustrate_me( )