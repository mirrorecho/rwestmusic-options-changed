import abjad
import calliope

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
        # TO DO... this should be implemented in some more consistent way on the base calliope.Event
        return abjad.NamedPitch(self.pitch).number

class Event1(CloselyEventMixin, calliope.Event):
    pitch = "D4"
    set_beats = 1

class Event2(CloselyEventMixin, calliope.Event):
    pitch = "F4"
    set_beats = 0.5

class Event3(CloselyEventMixin, calliope.Event):
    pitch = "E4"
    set_beats = 0.5

class Event4(CloselyEventMixin, calliope.Event):
    pitch = "G4"
    set_beats = 1

class Event5(CloselyEventMixin, calliope.Event):
    pitch = "Ab4"
    set_beats = 1

# ==============================

calliope.illustrate_me()
