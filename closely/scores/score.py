import calliope

# WARNING WARNING WARNING... THIS CREATES DUPE NAMED ITEMS IN MODULE BUBBLE TREE AND MESSES THING UP!!!!!!!!
# from closely.score_staves import CloselyScore
from closely.scores import score_staves

# from mark_0 import score_0
# from mark_a import score_a
# from mark_b import score_b
from closely.mark_c import score_c
from closely.mark_d import score_d
# from mark_e import score as score_e
# from mark_f import score as score_f
# from mark_g import score as score_g
# from mark_h import score as score_h

closely_score_music = calliope.MatchSequence(
    # calliope.Bubble.from_module(score_0, name="score_0"),
    # calliope.Bubble.from_module(score_a, name="score_a"),
    # calliope.Bubble.from_module(score_b, name="score_b"),
    score_c.mark_c_score,
    score_d.mark_d,
    # calliope.Bubble.from_module(score_d, name="score_d"),
    # calliope.Bubble.from_module(score_e, name="score_e"),
    # calliope.Bubble.from_module(score_f, name="score_f"),
    # calliope.Bubble.from_module(score_g, name="score_g"),
    # calliope.Bubble.from_module(score_h, name="score_h"),
)

calliope.illustrate_me(
    bubble=closely_score_music.get_inverted(), 
    score_type=score_staves.CloselyScore,
    as_midi = True,
    )

