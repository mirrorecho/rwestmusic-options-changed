import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers)

# _______________________________________________________________________________
# _______________________________________________________________________________
# PHRASES:

PITCH_SELECT_C = pitches.with_reversed(pitches.PITCH_SELECT_STUTTER)
PITCH_SELECT_DOWN_C = pitches.down(pitches.PITCH_SELECT_WAVER)

class CPhrase(sequences.PhraseFactory):
    pitch_sequence = pitches.PITCH_SEQUENCE.select(*PITCH_SELECT_C)
    rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN

class CPhraseFast(sequences.PhraseFactory):
    pitch_sequence = pitches.PITCH_SEQUENCE.select(*PITCH_SELECT_C[:7])
    rhythm_pattern = rhythms.FAST_RHYTHM_PATTERN

class CPhraseFastDown(CPhraseFast):
    pitch_sequence = pitches.PITCH_SEQUENCE.select(*PITCH_SELECT_DOWN_C)

# _______________________________________________________________________________
# _______________________________________________________________________________
# LineBlocks:

class BlockC(calliope.LineStacked):
    child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
    intervals = pitches.CHORDS_ALT

    class AddConstantPitch(sequences.TransformAddConstantPitch):
        pitch = 0

    class PitchesThroughGrid(calliope.PitchesThroughGrid):
        tally_apps = tally_apps_lib.LINE_TALLY_APPS
        pitch_ranges = pitch_range_helpers.hill_ranges_maker(6)

    def tally_pitches(self):
        self.pitch_grid.tally_loop()
        self.transforms_tree["PitchesThroughGrid"].transform_nodes(self)

# TO DO... able to get rid of the nested clases below?

class BlockC_I(BlockC):
    class MyPhrase(CPhrase):
        rhythm_lengths = (9,9)
        bookend_rests = (4,)
        fill_rests = True

class BlockC_II(BlockC):
    class MyPhrase(BlockC_I.MyPhrase):
        rhythm_lengths = (13,)
        bookend_rests = (6,)
    class AddConstantPitch(BlockC.AddConstantPitch):
        pitch = -2

class BlockC_III(BlockC_II):
    intervals = pitches.CHORDS_FOURTHS
    class MyPhrase(CPhraseFast):
        rhythm_lengths = (4,3)
        bookend_rests = (3,)

class BlockC_IV(BlockC):
    intervals = BlockC.intervals
    class MyPhrase(CPhraseFast):
        rhythm_lengths = (3,3,3)
        pitch_sequence_index = 7
        bookend_rests = (1,)

class BlockC_V(BlockC_IV):
    intervals = pitches.CHORDS_ALT_MAJOR
    class MyPhrase(CPhraseFastDown):
        rhythm_lengths = (3,2,2)
        bookend_rests = (3,)

class BlockC_VI(BlockC_V):
    class MyPhrase(BlockC_V.MyPhrase):
        bookend_rests = (1,)
    class AddConstantPitch(BlockC.AddConstantPitch):
        pitch = 2

class BlockC_VII(BlockC):
    intervals = pitches.CHORDS_FOURTHS
    class MyPhrase(CPhraseFastDown):
        rhythm_lengths = (8,)
        bookend_rests = (1,)
        pitch_sequence_index = 1
        transpose=12
    class AddConstantPitch(BlockC.AddConstantPitch):
        pitch = 4

class BlockC_VIII(BlockC_VII):
    class MyPhrase(CPhraseFast):
        rhythm_lengths = (10,)
        pitch_sequence = pitches.PITCH_SEQUENCE_DOWN
        pitch_sequence_index = -3
        transpose=12
    class AddConstantPitch(BlockC.AddConstantPitch):
        pitch = 6

class BlockC_IX(BlockC):
    intervals = pitches.CHORDS_MAJOR
    class MyPhrase(sequences.PhraseFactory):
        rhythm_lengths = (9,)
        rhythm_pattern = rhythms.STRAIGHT_RHYTHM_PATTERN
        pitch_sequence = pitches.PITCH_SEQUENCE_DOWN
        pitch_sequence_index = 3
        transpose=12
    class AddConstantPitch(BlockC.AddConstantPitch):
        pitch = -1

c_i = BlockC_I(name="c_i")
c_ii = BlockC_II(name="c_ii")
c_iii = BlockC_III(name="c_iii")
c_iv = BlockC_IV(name="c_iv")
c_v = BlockC_V(name="c_v")
c_vi = BlockC_VI(name="c_vi")
c_vii = BlockC_VII(name="c_vii")
c_viii = BlockC_VIII(name="c_viii")
c_ix = BlockC_IX(name="c_ix")
c_x = c_ix(name="c_x")

c_sequence = (c_i, c_ii, c_iii, c_iv, c_v, c_vi, c_vii, c_viii, c_ix, c_x)

# c_i.transform_through_pitch_grid.grid.illustrate_start()
# c_i.transform_through_pitch_grid.grid.illustrate_me()
# c_vi.illustrate_me()


