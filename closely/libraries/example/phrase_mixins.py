import abjad
from calliope import tools, structures, bubbles, machines
from closely.libraries import events, cells

class FastMixin(calliope.TreeMixin):
    class MakeFast(calliope.Transform):
        def transform_nodes(self, machine):
            for m in machine.leaves:
                if m.beats > 0.5 and not m.rest:
                    m.beats = 0.5


class MinSpacingMixin(calliope.TreeMixin):
    class AddMinSpacing(calliope.Transform):
        min_spacing = 0.5
        def transform_nodes(self, machine):
            for m in machine.leaves:
                if m.beats < self.min_spacing and m.rest:
                    m.beats = self.min_spacing