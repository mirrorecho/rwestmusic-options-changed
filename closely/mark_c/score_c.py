import abjad
import calliope

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely.scores import score_staves

from closely.mark_c.material_c import c_sequence

# TEMPO = 120
# so 30 measures of 4/4 needed

class LineC(calliope.Line):
    show_cells = calliope.BracketCells()
    metrical_durations = ( (2,4,),(2,4,),) * 30

class MarkC(calliope.LineBlock):
    class Flute(LineC): pass
    class Clarinet(LineC): pass
    class Violin(LineC): pass
    class Cello(LineC): pass

    # NOTE: a little funky.... but this might work well
    # for i, part_cls in enumerate([Flute, Clarinet, Violin, Cello]):
    #     for block in c_sequence:
    #         setattr(part_cls, "phrase_" + block.name, block[i])

# _____________________________________________________________________________________

mark_c_score = MarkC(name="mark_c")

for i, part in enumerate(mark_c_score):
    for block in c_sequence:
        part["phrase_" + block.name] = block[i]()
    calliope.BracketCells().transform_nodes(machine=part)

mark_c_score["Flute"]["phrase_c_ix"].logical_ties[0].beats=2
mark_c_score["Clarinet"]["phrase_c_ix"].logical_ties[0].beats=2
mark_c_score["Violin"]["phrase_c_ix"].logical_ties[0].beats=2
mark_c_score["Cello"]["phrase_c_ix"].logical_ties[0].beats=2

mark_c_score["Flute"]["phrase_c_x"].logical_ties[-1].beats=4
mark_c_score["Clarinet"]["phrase_c_x"].logical_ties[-1].beats=4
mark_c_score["Violin"]["phrase_c_x"].logical_ties[-1].beats=4
mark_c_score["Cello"]["phrase_c_x"].logical_ties[-1].beats=4

# _____________________________________________________________________________________

calliope.illustrate_me(bubble=mark_c_score, score_type=score_staves.CloselyScore, as_midi=True)