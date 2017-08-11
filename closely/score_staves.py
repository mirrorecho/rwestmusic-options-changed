import abjad
from calliope import bubbles

class CloselyScore(bubbles.Score):

    class Flute(bubbles.Staff):
        instrument=abjad.instrumenttools.Flute(
            instrument_name="Flute", short_instrument_name="fl.")

    class Clarinet(bubbles.Staff):
        instrument=abjad.instrumenttools.ClarinetInBFlat(
            instrument_name="Clarinet in Bb", short_instrument_name="cl.")

    class Violin(bubbles.Staff):
        instrument=abjad.instrumenttools.Violin(
            instrument_name="Violin", short_instrument_name="vln.")

    class Cello(bubbles.Staff):
        instrument=abjad.instrumenttools.Cello(
            instrument_name="Cello", short_instrument_name="vc.")
        clef="bass"
