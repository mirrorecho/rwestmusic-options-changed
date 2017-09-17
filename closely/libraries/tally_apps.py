import calliope

LINE_TALLY_APPS = (
    calliope.TallyCircleOfFifthsRange(over_range_multiplier=-99), 
    calliope.TallyParallelIntervals(interval_ratings=[(0,-20), (7,-11)]), 
    calliope.TallyMelodicIntervals(
            interval_ratings=[(0, -200), (1,80), (2,90), (3,60), (4,50), (5,6), (6,-20), (7,-4), (10,-30), (11,-50), (12,-4)], 
            over_incremental_multiplier=(12,-80),
            # up_rating=-12,
            # down_rating=20,
            ),
    calliope.TallyRepeatedJumps(),
    )