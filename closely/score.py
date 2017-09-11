import calliope
from score_staves import CloselyScore
from mark_0 import score as score_0
from mark_a import score as score_a
from mark_b import score as score_b
from mark_c import score as score_c
from mark_d import score as score_d
from mark_e import score as score_e
from mark_f import score as score_f
from mark_g import score as score_g
from mark_h import score as score_h

closely_score_music = calliope.MatchSequence(
    calliope.Bubble.from_module(score_0, name="score_0"),
    # calliope.Bubble.from_module(score_a, name="score_a"),
    # calliope.Bubble.from_module(score_b, name="score_b"),
    # calliope.Bubble.from_module(score_c, name="score_c"),
    # calliope.Bubble.from_module(score_d, name="score_d"),
    # calliope.Bubble.from_module(score_e, name="score_e"),
    # calliope.Bubble.from_module(score_f, name="score_f"),
    # calliope.Bubble.from_module(score_g, name="score_g"),
    # calliope.Bubble.from_module(score_h, name="score_h"),
)

calliope.illustrate_me(bubble=closely_score_music, score_type=CloselyScore)

