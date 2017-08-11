import abjad
from calliope import tools, bubbles, machines
from closely.libraries import events, cells, phrases

class StackedTransform(machines.Transform):
    def transform_nodes(self, machine):
        new_lines = []
        for i in range(len(machine.intervals[0])):
            for line in machine:
                stack_line = line(name=line.name + "_%s" % i )
                for e, event in enumerate(stack_line.events):
                    # TO DO... assumes that there are no chords... also may want
                    # a more generalized transpose on event / logical tie
                    event.transpose(machine.intervals[e % len(machine.intervals)][i])
                new_lines.append(stack_line)
        machine[:] = new_lines



class LineStacked(machines.LineBlock):
    intervals = ( (12,12), (7,12) )
    swaps = ()
    # line_1 = machines.Line( machines.Event(beats=2, pitch="A4") )
    stack_me = StackedTransform()
    
    def swap_events(self, swaps=()):
        swaps = swaps or self.swaps
        for s, swap in enumerate(swaps):
            new_vertical = [ self[swap_value].events[s] for swap_value in swap ]
            print([v.pitch for v in new_vertical])
            for i, event in enumerate(new_vertical):
                # TO DO, this is screwy, inelegant, and confusing: rethink...
                event_index = self[i].events[s].my_index
                self[i].events[s].parent[event_index] = event()


    # transpose_me = machines.Transpose(interval=2)

class TestLineStacked(LineStacked):
    intervals = ( (0,2,3,7,12), (0,2,7,9,12), ) 
    swaps = (
        (4,3,2,1,0),
        # (2,1,4,3,0),
        (0,1,2,3,4),
        )
    my_line1 = machines.Line( cells.CloselyCell() )
    # my_line2 = machines.Line( cells.CloselyCell() )

t = TestLineStacked()
t.swap_events()


# ============================================================

tools.illustrate_me( bubble=t )
