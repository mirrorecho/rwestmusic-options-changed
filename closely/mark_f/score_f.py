import abjad
import calliope

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely.scores import score_staves

from closely.mark_f import material_f

# TEMPO = 120
# so 30 measures of 4/4 needed

class LineF(calliope.Line):
    show_cells = calliope.BracketCells()
    metrical_durations = ( (2,4,),(2,4,),) * 32

class MarkF(calliope.LineBlock):
    class Flute(LineF): pass
    class Clarinet(LineF): pass
    class Violin(LineF): pass
    class Cello(LineF): pass

# _____________________________________________________________________________________

mark_f = MarkF(name="mark_f")

for i, part in enumerate(mark_f):
    for block in material_f.f_sequence:
        part["phrase_%s_%s" % (block.name, i)] = block[i]() # TO DO: this copy is screwy... maybe it can be removed eventually?
    # calliope.BracketCells().transform_nodes(machine=part)

# _____________________________________________________________________________________

# calliope.illustrate_me(bubble=material_d.d_star_iii)

calliope.illustrate_me(bubble=mark_f, score_type=score_staves.CloselyScore, as_midi=True)
