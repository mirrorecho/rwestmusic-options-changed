import math
import abjad
import calliope

class SymmetricalRhythmPattern(calliope.CalliopeBaseMixin):
    end_offset = 0
    pattern = ()
    filler = ( (1,), )

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setup(**kwargs)

    def get_pattern(self, *args, **kwargs):
        return self.pattern

    def get_filler(self, *args, **kwargs):
        return self.filler


    def __call__(self, length, *args, **kwargs):
        pattern = self.get_pattern(*args, **kwargs)
        filler = self.get_filler(*args, **kwargs)
        start_length = math.floor(length/2) + self.end_offset
        end_length = length - start_length
        start = pattern[:start_length]
        end = pattern[self.end_offset : end_length + self.end_offset][::-1]
        middle = tuple([
            filler[i % len(filler)] for i in range(length - len(start) - len(end))
            ])
        rhythm = [beats for beat in start + middle + end for beats in beat] 
        return_list = []
        rest_beats = 0
        for b in rhythm:
            if b > 0:
                if rest_beats < 0:
                    return_list.append(rest_beats)
                return_list.append(b)
                rest_beats = 0
            else:
                rest_beats += b
        if rest_beats < 0:
            return_list.append(rest_beats)
        return tuple(return_list)

DRONE_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (1,), (2,), (3,) ),
    filler=( (4,), ),
    )
DRILL_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.5,0.5,), (1,), (1,) ),
    filler=( (-1,), ),
    )

FLIT_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.25,0.25), (-0.5,), (0.25,0.25), ),
    filler=( (-0.5,), ),
    )

# s = SymmetricalBeats()
# print(s(6))