import math
import abjad
import calliope

from closely.libraries import pitches, rhythms


class SequenceMixin(object):
    rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
    pitch_sequence = pitches.PITCH_SEQUENCE
    rhythm_lengths = (5,5,5,5)
    fill_rests = False
    pitch_sequence_index=0

    def get_pitch_sequence(self):
        return self.pitch_sequence


class SequenceFactory(SequenceMixin, calliope.Factory):

    def get_branches_kwargs(self, *args, **kwargs):
        pitch_sequence = self.get_pitch_sequence()
        pitch_sequence_index = self.pitch_sequence_index
        kwargs_list = []

        for rl in self.rhythm_lengths:
            rhythm = self.rhythm_pattern(rl, fill_rests=self.fill_rests)
            pitches_length = len(list(filter(lambda x: x>0, rhythm)))
            kwargs_list.append(dict(
                rhythm = rhythm,
                pitches = pitch_sequence[pitch_sequence_index : pitch_sequence_index+pitches_length],
                pitches_skip_rests = True
                ))
            pitch_sequence_index += pitches_length

        return kwargs_list




class DroneSequenceFactory(SequenceFactory):
    pitch_sequence = calliope.PitchSequence()


class SeePitches(SequenceFactory, calliope.Cell):
    rhythm_pattern = rhythms.STRAIGHT_RHYTHM_PATTERN

    def __init__(self, pitch_sequence, chords=None, *args, **kwargs):
        self.rhythm_lengths = (0, pitch_sequence.cyclic_length)
        if chords:
            chords_sequence = []
            for p in range(pitch_sequence.cyclic_length):
                chords_sequence.append([c + pitch_sequence[p] for c in chords[p % len(chords)]])
            self.pitch_sequence = chords_sequence
        else:
            self.pitch_sequence = pitch_sequence
        super().__init__(*args, **kwargs)

