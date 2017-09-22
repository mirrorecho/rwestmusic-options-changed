import abjad
import calliope

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely import score_staves

from closely.mark_d import material_d

# TEMPO = 120
# so 30 measures of 4/4 needed

class LineD(calliope.Line):
    show_cells = calliope.BracketCells()
    metrical_durations = ( (2,4,),(2,4,),) * 30

class MarkD(calliope.LineBlock):
    class Flute(LineD): pass
    # class Clarinet(LineD): pass
    # class Violin(LineD): pass
    # class Cello(LineD): pass

# _____________________________________________________________________________________

mark_d = MarkD()

for i, part in enumerate(mark_d):
    for block in material_d.d_sequence:
        part["phrase_%s_%s" % (block.name, i)] = block[i]
    calliope.BracketCells().transform_nodes(machine=part)

# _____________________________________________________________________________________


calliope.illustrate_me(bubble=material_d.d_star_iii)

# calliope.illustrate_me(bubble=mark_d, score_type=score_staves.CloselyScore)
