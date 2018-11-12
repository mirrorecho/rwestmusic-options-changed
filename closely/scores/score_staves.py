import abjad
import calliope

class CloselyScore(calliope.Score):
    stylesheets=("../../stylesheets/score.ily",)

    class Violin1(calliope.Staff):
        instrument=abjad.Violin(
            name="Violin 1", short_name="vln.1")

    class Violin2(calliope.Staff):
        instrument=abjad.Violin(
            name="Violin 2", short_name="vln.2")

    class Viola(calliope.Staff):
        instrument=abjad.Viola(
            name="Viola", short_name="vla.")

    class Cello(calliope.Staff):
        instrument=abjad.Cello(
            name="Cello", short_name="vc.")
        clef="bass"
