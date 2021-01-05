import math
import abjad
import calliope

from closely.libraries import (pitches, sequences, rhythms, 
    tally_apps_lib, pitch_range_helpers, phrases)


class PhraseTranspose(calliope.Transpose):
    line = 0
    def transform_nodes(self, machine):
        calliope.Transpose.transform_nodes(self, machine[self.line])

class PhraseRhythm(calliope.Transform):
    line = 0
    rhythm = (1,)
    def transform_nodes(self, machine):
        machine[self.line].rhythm = self.rhythm

class PhraseOsti(PhraseRhythm):
    rhythm = ( # TO DO... shouldn't be allowed to make up this rhythm here!
        -1,2,1,1,1,2,2,
        -1,2,1,2,2
        )
    def transform_nodes(self, machine):
        super().transform_nodes(machine)
        # machine[self.line].rhythm = self.rhythm

class PhraseChopRhythm(calliope.Transform):
    line = 0
    def transform_nodes(self, machine):
        for e in machine[self.line].note_events:
            my_tie = e.first_non_rest
            my_tie.ticks = int(my_tie.ticks / 2)
            e.append(my_tie())

class BookendRests(calliope.Transform):
    bookend_rests = (None, None)
    def transform_nodes(self, machine):
        for phrase_line in machine:
            phrase_line.add_bookend_rests(*self.bookend_rests)

class SwapPhraseLines(calliope.Transform):
    swap = (0,1)
    def transform_nodes(self, machine):
        machine[self.swap[0]],machine[self.swap[1]] = machine[self.swap[1]](),machine[self.swap[0]]()

# TO DO: this might be better to use in calliope generally
def split_events(machine, split_beats=0.5):
    for e in machine.note_events:
        if e.beats > split_beats:
            event_index = e.my_index
            e.parent[event_index:event_index+1] = [
                e(rhythm=(split_beats,)) for s in range( math.ceil(e.beats / split_beats)) 
                ]

class FStarTransform(calliope.Transform):
    respell = None
    bracket_cells = calliope.BracketCells()

    def transform_nodes(self, machine):
        for phrase_line in machine:
            if self.respell:
                phrase_line.respell = self.respell

class FStarI(phrases.StarPhraseBlockI):
    # transpose_up = calliope.Transpose(interval=1)

    class TransformMe(FStarTransform): 
        respell = "flats"
        class SwapFluteViolin(SwapPhraseLines):
            swap = (0,2)
        class CelloDown(PhraseTranspose):
            line = 3
            interval = -12
        class ViolinFlatRhythm(PhraseOsti):
            line = 2
        class CelloFlatRhythm(PhraseOsti):
            line = 3
        class ViolinChopRhythm(PhraseChopRhythm):
            line = 2
        class CelloChopRhythm(PhraseChopRhythm):
            line = 3

class FStarII(phrases.StarPhraseBlockII):
    class TransformMe(FStarTransform): 
        respell = "flats"
        class SwapFluteViolin(SwapPhraseLines):
            swap = (0,2)
        class CelloDown(PhraseTranspose):
            line = 3
            interval = -12
        class PauseBefore(BookendRests):
            bookend_rests = (1,)

class FStarIII(phrases.StarPhraseBlockIII):
    class TransformMe(FStarTransform): 
        respell = "flats"
        class SwapViolinCello(SwapPhraseLines):
            swap = (2,3)
        class FluteUp(PhraseTranspose):
            line = 0
            interval = 12
        class CelloDown(PhraseTranspose):
            line = 3
            interval = -24
        class PauseBefore(BookendRests):
            bookend_rests = (1,)
        class ExtendEnd(calliope.Transform):
            def transform_nodes(self, machine):
                for phrase_line in machine:
                    phrase_line.note_events[-1].first_non_rest.beats = 3
        class MiscOctaves(calliope.Transform):
            def transform_nodes(self, machine):
                machine[2].note_events[-1].pitch += 12
        class MiscRespell(calliope.Transform):
            def transform_nodes(self, machine):
                machine[3].respell = "sharps"
                flute_events = machine[0].note_events
                flute_events[-1].respell = "sharps"
                flute_events[-2].respell = "sharps"

class FStarIV(phrases.GridMask, phrases.StarPhraseBlock_I_Grid_A):
    transpose_up = calliope.Transpose(interval=1)
    pitches_from_grid_bubble = phrases.star_i_a_1
    class TransformMe(FStarTransform): 
        respell = "sharps"
        class ClarinetUp(PhraseTranspose):
            line = 1
            interval = 12
        class ViolinUp(PhraseTranspose):
            line = 2
            interval = 12
        class MiscOctaves(calliope.Transform):
            def transform_nodes(self, machine):
                machine[1].note_events[0].pitch -= 12

class FStarV(phrases.GridMask, phrases.StarPhraseBlock_II_Grid_A):
    transpose_up = calliope.Transpose(interval=1)
    pitches_from_grid_bubble = phrases.star_ii_a_1
    class TransformMe(FStarTransform): 
        respell = "sharps"
        class RemoveFirstCell(calliope.Transform):
            def transform_nodes(self, machine):
                for phrase_line in machine:
                    phrase_line.pop(0)
        class PauseBefore(BookendRests):
            bookend_rests = (2,)

class FStarVI(phrases.GridMask, phrases.StarPhraseBlock_III_Grid_A):
    transpose_up = calliope.Transpose(interval=1)
    pitches_from_grid_bubble = phrases.star_iii_a_1
    class TransformMe(FStarTransform): 
        respell = "sharps"
        class PauseBefore(BookendRests):
            bookend_rests = (1,)
        class ExtendEnd(calliope.Transform):
            def transform_nodes(self, machine):
                for phrase_line in machine:
                    phrase_line.note_events[-1].first_non_rest.beats = 3
class FStarVII(FStarIV):
    transpose_up = calliope.Transpose(interval=2)
    class TransformMe(FStarTransform): 
        respell = "flats"
        class SplitBeats(calliope.Transform):
            def transform_nodes(self, machine):
                for phrase_line in machine:
                    split_events(phrase_line[0])


f_star_i = FStarI(name="f_star_i")
f_star_ii = FStarII(name="f_star_ii")
f_star_iii = FStarIII(name="f_star_iii")
f_star_iv = FStarIV(name="f_star_iv")
f_star_v = FStarV(name="f_star_v")
f_star_vi = FStarVI(name="f_star_vi")
f_star_vii = FStarVII(name="f_star_vii")

# swap positions of lines 0 and 2
# (f_star_i[0],f_star_i[2],) = (f_star_i[2](),f_star_i[0](),) 
# TO DO... this implementation of transpose is a little screwy
# calliope.Phrase.transpose(f_star_i[3],-12)

f_sequence = (
    f_star_i,
    f_star_ii,
    f_star_iii,
    f_star_iv,
    f_star_v,
    f_star_vi,
    f_star_vii,
    )


calliope.illustrate_me(bubble=f_star_vii)