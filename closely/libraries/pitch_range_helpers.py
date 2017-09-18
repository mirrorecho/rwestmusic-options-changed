import pandas as pd
import calliope

def hill_range(start, steps, increment=1, span=12):
    hill_range = [start + increment*i for i in range(steps)]
    hill_range += reversed(hill_range)
    return [(b, b+span) for b in hill_range]

def hill_ranges_maker(steps, span=13):
    return pd.DataFrame.from_records([
                hill_range(5, steps, 2, span), # flute
                hill_range(-4, steps, 2, span), # clarinet
                hill_range(9, steps, -3, span), # viola
                hill_range(-3, steps, -3, span), # cello
            ])

def mid_ranges_maker():
    return pd.DataFrame.from_records([
                [ (9, 23), ], # flute
                [ (0, 16), ], # clarinet
                [ (-6, 14), ], # viola
                [ (-15, 5), ], # cello
            ])

