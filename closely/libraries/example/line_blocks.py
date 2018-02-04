import abjad
import calliope
from closely.libraries import events, cells

class TestLineStacked(calliope.LineStacked):
    intervals = ( (0,2,3,7,12), (0,2,7,9,12), ) 
    # swaps = (
    #     (4,3,2,1,0),
    #     (0,1,2,3,4),
    #     )
    my_line1 = calliope.Line( cells.CloselyCell() )
    # my_line2 = calliope.Line( cells.CloselyCell(transpose) )


# t = TestLineStacked(name="cloud_test")

# print(t.get_output_path(sub_directory="data") )

# print( t.get_calling_module().__file__)
# calliope.illustrate_me( bubble=TestLineStacked )