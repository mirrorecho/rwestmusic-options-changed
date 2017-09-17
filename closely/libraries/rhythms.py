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


    def __call__(self, length, fill_rests=False, *args, **kwargs):
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
        for i, b in enumerate(rhythm):
            if b > 0:
                if rest_beats < 0:
                    if fill_rests and len(return_list) > 0:
                        return_list[-1] -= rest_beats
                    else:
                        return_list.append(rest_beats)
                return_list.append(b)
                rest_beats = 0
            else:
                rest_beats += b
        if rest_beats < 0:
            if fill_rests and len(return_list) > 0:
                return_list[-1] -= rest_beats
            else:
                return_list.append(rest_beats)
        return tuple(return_list)

SIMPLE_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.5, 0.5,), ),
    filler=( (1,), ),
    )

SIMPLE_BROKEN_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.5,0.5,), (1,), (1,) ),
    filler=( (-1,), ),
    )

SLOW_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (1,), (2,), (3,) ),
    filler=( (4,), ),
    )

FLUTTER_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.25,0.25), (-0.5,), (0.25,0.25), ),
    filler=( (-0.5,), ),
    )

BUILD_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (0.5,0.5,), (0.5,0.5,),  ),
    filler=( (1,), ),
    )

# MEANINGFUL?
UPBEAT_SPACED_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (-0.5, 0.5,), (-1,), (0.5,-0.5,), (-1,)  ),
    filler=( (-0.5, 0.5,), ),
    )

UPBEAT_CLOCK_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (1,), ),
    filler=( (-0.5, 0.5,), ),
    )

FAST_RHYTHM_PATTERN = SymmetricalRhythmPattern(
    pattern=( (-0.5, 0.5,), ),
    filler=( (0.5, 0.5,), ),
    )

# print(UPBEAT_CLOCK_RHYTHM_PATTERN(6))
# print(UPBEAT_CLOCK_RHYTHM_PATTERN(6, fill_rests=True))

# s = SymmetricalBeats()
# print(s(6))