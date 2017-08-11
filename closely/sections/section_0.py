from calliope import tools, bubbles, machines
from closely import score_staves
from closely.libraries import phrases, phrase_mixins, cells

class BaseSection0(machines.Line):
    # metrical_durations = 
    pass

class Flute(BaseSection0):
    class LicksPhrase1(phrases.LicksPhrase): pass

class Clarinet(BaseSection0):
    class LicksPhrase1(
        phrase_mixins.FastMixin,
        phrase_mixins.MinSpacingMixin,
        phrases.LicksPhrase
        ):
        bookend_rests = (2,0)




# ============================================================

tools.illustrate_me(score_type=score_staves.CloselyScore)