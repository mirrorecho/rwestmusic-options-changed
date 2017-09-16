import pandas as pd
import calliope

# sub-class cell-block in order to auto-determine output path
class MyCellBlock(calliope.CellBlock): pass

c1 = MyCellBlock(
    calliope.Cell(rhythm=(1,1,2,4), pitches=(0,2,4,6)),
    calliope.Cell(rhythm=(1,1,2,4), pitches=(11,12,11,12)),
    calliope.Cell(rhythm=(1,1,2,4), pitches=(11,12,11,12)),
    name="c1",
    )

g = calliope.PitchGrid.from_bubble(c1)

