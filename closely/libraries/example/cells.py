import abjad
import calliope
from closely.libraries import events

class CloselyCell(calliope.Cell):
    class Event1(calliope.Event):
        pitch = "D4"
        set_beats = 1

    class Event2(calliope.Event):
        pitch = "F4"
        set_beats = 0.5

    class Event3(calliope.Event):
        pitch = "E4"
        set_beats = 0.5

    class Event4(calliope.Event):
        pitch = "G4"
        set_beats = 1

    class Event5(calliope.Event):
        pitch = "Ab4"
        set_beats = 1

class CloselyCellTr2(CloselyCell):
   transpose_2 = calliope.Transpose(interval=2)

class CloselyCellDisplaced(CloselyCell):
    class Event1(CloselyCell.Event1):
        transpose_fifths = calliope.DisplaceFifths(1)
    class Event2(CloselyCell.Event2):
        class MyTransposeFifthsDown(calliope.DisplaceFifths):
            multiple = -1
        # transpose_fifths = calliope.DisplaceFifths(-1)
        traspose_displace = calliope.Displace(1)

class UpLickMixin(calliope.TreeMixin):
    set_rhythm = (0.25,)*4 + (2,)
    sort_me = calliope.SortByPitch()
    class RemoveChildren(calliope.Remove): pass
    slur_me = calliope.Slur(0, -2)

class UpLick(UpLickMixin, CloselyCell): pass        

class UpLickDisplaced(UpLickMixin, CloselyCellDisplaced):
    set_rhythm = (0.25,)*3 + (2,)
    class RemoveChildren(calliope.Remove):
        args = (0,)

class CloselyStacked1(CloselyCell):
    my_chords = calliope.MakeChords( indices=[0, (1,2), (3,4)] )
    # set_rhythm = CloselyCell().rhythm[:3]

# ==============================

class BiggerCell(calliope.Cell):
    class SubCell1(CloselyCell): pass
    class SubCell2(CloselyCell): pass
    class SubCell3(CloselyCell): pass
    class SubCell4(CloselyCell): pass

calliope.illustrate_me()
