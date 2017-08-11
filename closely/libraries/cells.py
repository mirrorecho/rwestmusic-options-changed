import abjad
from calliope import tools, structures, bubbles, machines
from closely.libraries import events

class CloselyCell(machines.Cell):
    class Event1(machines.Event):
        pitch = "D4"
        set_beats = 1

    class Event2(machines.Event):
        pitch = "F4"
        set_beats = 0.5

    class Event3(machines.Event):
        pitch = "E4"
        set_beats = 0.5

    class Event4(machines.Event):
        pitch = "G4"
        set_beats = 1

    class Event4a(machines.Event):
        pitch = None
        set_beats = 1

    class Event5(machines.Event):
        pitch = "Ab4"
        set_beats = 1

class CloselyCellTr2(CloselyCell):
   transpose_2 = machines.Transpose(interval=2)

class CloselyCellDisplaced(CloselyCell):
    class Event1(CloselyCell.Event1):
        transpose_fifths = machines.DisplaceFifths(1)
    class Event2(CloselyCell.Event2):
        class MyTransposeFifthsDown(machines.DisplaceFifths):
            multiple = -1
        # transpose_fifths = machines.DisplaceFifths(-1)
        traspose_displace = machines.Displace(1)

class UpLickMixin(structures.TreeMixin):
    set_rhythm = (0.25,)*4 + (2,)
    sort_me = machines.SortByPitch()
    class RemoveChildren(machines.Remove): pass
    slur_me = machines.Slur(0, -2)

class UpLick(UpLickMixin, CloselyCell): pass        

class UpLickDisplaced(UpLickMixin, CloselyCellDisplaced):
    set_rhythm = (0.25,)*3 + (2,)
    class RemoveChildren(machines.Remove):
        args = (0,)

# class CloselyStacked1(CloselyCell):
#     my_chords = machines.MakeChords( indices=[0, (1,2), (3,4)] )
#     # set_rhythm = CloselyCell().rhythm[:3]

# ==============================

tools.illustrate_me()