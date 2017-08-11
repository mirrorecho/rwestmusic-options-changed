import abjad
from calliope import tools, bubbles, machines

class CloselyEventMixin(object):
    displace_fifths = 0
    displace_octaves = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.displace_fifths:
            self.pitch = abjad.NamedPitch(self.pitch).transpose(self.displace_fifths * 7)
        if self.displace_octaves:
            self.pitch = abjad.NamedPitch(self.pitch).transpose(self.displace_octaves * 12)

    def get_pitch_number(self):
        # TO DO... this should be implemented in some more consistent way on the base machines.Event
        return abjad.NamedPitch(self.pitch).number

class Event1(CloselyEventMixin, machines.Event):
    pitch = "D4"
    set_beats = 1

class Event2(CloselyEventMixin, machines.Event):
    pitch = "F4"
    set_beats = 0.5

class Event3(CloselyEventMixin, machines.Event):
    pitch = "E4"
    set_beats = 0.5

class Event4(CloselyEventMixin, machines.Event):
    pitch = "G4"
    set_beats = 1

class Event5(CloselyEventMixin, machines.Event):
    pitch = "Ab4"
    set_beats = 1

# ==============================

tools.illustrate_me()
