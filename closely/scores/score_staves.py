import abjad
import calliope

class CloselyScore(calliope.Score):
    stylesheets=("../../stylesheets/score.ily",)

    class Violin1(calliope.Staff):
        instrument=abjad.instrumenttools.Violin(
            instrument_name="Violin 1", short_instrument_name="vln.1")

    class Violin2(calliope.Staff):
        instrument=abjad.instrumenttools.Violin(
            instrument_name="Violin 2", short_instrument_name="vln.2")

    class Viola(calliope.Staff):
        instrument=abjad.instrumenttools.Viola(
            instrument_name="Viola", short_instrument_name="vla.")

    class Cello(calliope.Staff):
        instrument=abjad.instrumenttools.Cello(
            instrument_name="Cello", short_instrument_name="vc.")
        clef="bass"
