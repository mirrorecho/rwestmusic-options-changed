import abjad
import calliope

import pitches, sequences, rhythms, tally_apps_lib, pitch_range_helpers
from closely.scores import score_staves

# # TO DO... CONSIDER MOVING TO CALLIOPE
# class GridMask(object):
#     """
#     TO DO: what is the meaning/use of this?
#     """
#     pitches_from_grid_bubble = None

#     class PitchesThroughGrid(calliope.Transform): pass

#     class PitchesFromGrid(calliope.Transform):
#         def transform_nodes(self, machine):
#             if machine.pitches_from_grid_bubble:
#                 for line_index, l in enumerate(machine):
#                     for event_index, event in enumerate([e for e in l.note_events]):
#                         # NOTE: grid will have numpy.int64 for each pitch, but machine expects int
#                         # ... change to use duck typing?
#                         event.pitch = int(machine.pitches_from_grid_bubble.pitch_grid.data.iat[line_index, event_index])


# # _______________________________________________________________________________

class StarPhrase(sequences.SequenceFactory, calliope.Phrase):
    pitch_sequence = pitches.PITCH_SEQUENCE_STAR(transpose=-12)
    rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
    rhythm_lengths = (3,3,3,)
    respell = "flats"

class StarPhraseBlock(calliope.StackPitches, calliope.PhraseBlzock):
    intervals = pitches.CHORDS_SEQUENCE_STAR

    def get_branch(*args, **kwargs):
        return StarPhrase()

star_block_d = StarPhraseBlock()

# d_score = CloselySection(calliope.Arrange, "D")
# d_score["violin"].arrange()
star_block_d.illustrate_me()


# print(s[0].events[4].ticks_before)
# print(s[1].events[4].ticks_before)

# print(s[0].cells)
# l = calliope.Line(*s[0].cells[:-1])
# s.illustrate_me()

# class CloselyMark(calliope.LineBlock):
#     class Violin1(calliope.Line): pass
#     class Violin2(calliope.Line): pass
#     class Viola(calliope.Line): pass
#     class Cello(calliope.Line): pass

# my_mark = CloselyMark("my_mark")
# my_mark["Violin1"].extend(s[0])


# s.select.setattrs(container_type=abjad.Staff)
# s.select[-1].tag("bass")
# s.select[-1].events[7].ta("treble")7

# my_mark.illustrate_me(score_type=score_staves.CloselyScore)

# StarPhrase().phrases[0].illustrate_me()

# s.illustrate_me()

# s = calliope.CellBlock(
#     calliope.Cell(rhythm=(1,1,1,1,3,2), 
#     pitches=(2,0,None,7,None,6)),
#     calliope.Cell(rhythm=(1,1,1,1,3,2), 
#     pitches=(-2,0,None,7,None,6)),
#     )

# calliope.SlurCells().transform(s)

# s[0].cells[0].tag("bass")
# s[0].cells[2].tag("treble")

# s.illustrate_me()

# p = calliope.PhraseBlock(
#     calliope.Phrase("yo1", pitches=(0,12), rhythm=(1,2)),
#     calliope.Phrase("yo2", pitches=(2,7), rhythm=(2,1)),
#     )

# print(s.ly())
# print(s.is_simultaneous)
# s.illustrate_me()
# p.illustrate_me()
# print(s.is_simultaneous)
# print(s.container_type)

# m = p.blow()
# print(m.is_simultaneous)
# print(format(m))

# calliope.illustrate_me(bubble=s)




# class StarPhraseI(StarPhrase):
#     rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN

# class StarPhraseII(StarPhrase):
#     rhythm_pattern = rhythms.CLOCK_RHYTHM_PATTERN

# class StarPhraseIII(StarPhrase):
#     rhythm_pattern = rhythms.UPBEAT_CLOCK_RHYTHM_PATTERN
# # _______________________________________________________________________________

# class StarRhythmPhrase(sequences.PhraseFactory):
#     rhythm_pattern = rhythms.UPBEAT_SPACED_RHYTHM_PATTERN
#     rhythm_lengths = (10,8)
#     fill_rests=True

# class SubRhythmPhrase(sequences.PhraseFactory):
#     rhythm_lengths = (4,4,6)
#     bookend_rests = (2,)
#     rhythm_pattern = rhythms.SIMPLE_RHYTHM_PATTERN
    
#     class SubRhythmMod(calliope.Transform):
#         # TO DO... this could more elegant... rethink fusing
#         def transform_nodes(self, machine):
#             for c in machine.cells:
#                 c[0].fuse(1)
#                 c[2].fuse(1)
#                 c[4].fuse(1)
#             machine.events[-2].fuse(1)
#             for c in machine.cells:
#                 c.remove_empty()
#             machine.cells[1].append(calliope.RestEvent(2))
#             machine.reset_pitches()
# # _______________________________________________________________________________

# basic block:
# class StarPhraseBlock(calliope.LineStacked):
#     # TO DO: should not have to specify child_types here...
#     child_types = (calliope.Line, calliope.Phrase, calliope.Cell)
#     intervals = pitches.CHORDS_SEQUENCE_STAR
#     class StarPhrase(StarPhrase):
#         rhythm_lengths = (10,8)

#     class AddConstantPitch(sequences.TransformAddConstantPitch):
#         pitch = -2

# # ____________________________

# class StarPhraseBlockI(StarPhraseBlock):
#     class StarPhrase(StarPhraseI):
#         rhythm_lengths = (10,8)
#         fill_rests = True

# class StarPhraseBlockII(StarPhraseBlock):
#     # TO CONSIDER... always apply rotation to intervals equivalent to pitch_sequence_index??
#     intervals = pitches.rotate(pitches.CHORDS_SEQUENCE_STAR, -5)
#     class StarPhrase(StarPhraseII):
#         rhythm_lengths = (5,7)
#         fill_rests = True
#         pitch_sequence_index = -5

# class StarPhraseBlockIII(StarPhraseBlock):
#     intervals = pitches.rotate(pitches.CHORDS_SEQUENCE_STAR, 6)
#     class StarPhrase(StarPhraseIII):
#         rhythm_lengths = (5,5)
#         fill_rests = True
#         pitch_sequence_index = 6
#         transpose=-12
# # _______________________________________________________________________________

# class StarGridMixin(StarPhraseBlock):
#     class PitchesThroughGrid(calliope.PitchesThroughGrid):
#         tally_apps = tally_apps_lib.LINE_SMOOTH_TALLY_APPS
#         pitch_ranges = pitch_range_helpers.mid_ranges_maker()
#     def tally_pitches(self):
#         self.pitch_grid.tally_loop()
#         self.transforms_tree["PitchesThroughGrid"].transform_nodes(self)

# class StarPhraseBlock_I_Grid_A(StarPhraseBlockI, StarGridMixin): pass
# class StarPhraseBlock_II_Grid_A(StarPhraseBlockII, StarGridMixin): pass
# class StarPhraseBlock_III_Grid_A(StarPhraseBlockIII, StarGridMixin): pass

# # star_i_a_1 = StarPhraseBlock_I_Grid_A(name="star_i_a")
# # star_i_a_2 = StarPhraseBlock_I_Grid_A(name="star_i_a", grid_version=2)
# # star_ii_a_1 = StarPhraseBlock_II_Grid_A(name="star_ii_a")
# # star_iii_a_1 = StarPhraseBlock_III_Grid_A(name="star_iii_a")

# # ============================================================

# # s2=calliope.Cell(*star_i_a_1.apply_selection(funny_selection).copy())

# # TO DO... why doesn't this work???
# # s2["show_cells"] = calliope.BracketCells()

# # star_i_a_1.illustrate_me()
# # s2.illustrate_me()


# calliope.illustrate_me(bubble=StarPhraseBlock)