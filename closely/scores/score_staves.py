import abjad
import calliope

class CloselyScore(calliope.Score):
    stylesheets=("../../stylesheets/score.ily",)

    class Flute(calliope.Staff):
        instrument=abjad.instrumenttools.Flute(
            instrument_name="Flute", short_instrument_name="fl.")

    class Clarinet(calliope.Staff):
        instrument=abjad.instrumenttools.ClarinetInBFlat(
            instrument_name="Clarinet in Bb", short_instrument_name="cl.")

    class Violin(calliope.Staff):
        instrument=abjad.instrumenttools.Violin(
            instrument_name="Violin", short_instrument_name="vln.")

    class Cello(calliope.Staff):
        instrument=abjad.instrumenttools.Cello(
            instrument_name="Cello", short_instrument_name="vc.")
        clef="bass"
