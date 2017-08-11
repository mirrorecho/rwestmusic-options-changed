import abjad
from calliope import tools, bubbles, machines
from closely.libraries import events, cells

class LicksPhrase(machines.Phrase):

    class Lick1(cells.UpLick):
        bookend_rests = (0, 0.25)

    class Lick2(cells.UpLickDisplaced): pass


# ============================================================

tools.illustrate_me()