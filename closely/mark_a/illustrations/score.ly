% 2017-09-11 02:41

\version "2.19.54"
\language "english"

\include "../../stylesheets/score.ily"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Flute" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Flute }
            \set Staff.shortInstrumentName = \markup { Fl. }
            {
                \accidentalStyle modern-cautionary
                r4
                c''16 \startGroup [
                g''16
                r8 ]
                c''16 [
                bf''16
                r8 ]
                r4
                {
                    R1 * 2
                }
                r2
                r8 [
                f''16
                bf''16 ]
                r8 [
                a''16
                ef''16 \stopGroup ]
                af''16 \startGroup [
                g''16
                r8 ]
                d''16 [
                g''16 \stopGroup
                r8 ]
                r2
                {
                    R1 * 7
                }
                r4. [
                c''16 \startGroup
                f''16
                r4
                g''16
                af''16 \stopGroup
                c''16 \startGroup
                c''16 ]
                r8 [
                bf''16
                ef''16
                r2. ]
                {
                    R1 * 1
                }
                f''16 [
                g''16
                r8 ]
                bf''16 [
                bf''16 \stopGroup
                a''16 \startGroup
                d''16 ]
                r8 [
                ef''16
                f''16 ]
                r4
                af''16 [
                a''16
                r8 ]
                g''16 [
                c''16 \stopGroup
                c''16 \startGroup
                f''16 ]
                r4
                g''16 [
                af''16 \stopGroup
                c''16 \startGroup
                c''16 ]
                r4
                bf''16 [
                ef''16 \stopGroup
                f''16 \startGroup
                g''16 ]
                r8 [
                bf''16
                bf''16 ]
                r4
                r8 [
                a''16
                d''16 ]
                r8 [
                ef''16
                f''16 \stopGroup ]
                c''16 \startGroup [
                f''16
                r8 ]
                g''16 [
                af''16
                c''16
                c''16 ]
                r8 [
                bf''16
                ef''16 \stopGroup ]
                f''16 \startGroup [
                g''16
                r8 ]
                bf''16 [
                bf''16
                a''16
                d''16 ]
                r8 [
                ef''16
                f''16 \stopGroup ]
            }
        }
        \context Staff = "Clarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                \accidentalStyle modern-cautionary
                {
                    R1 * 3
                }
                r2
                r4
                r8 [
                c'16 \startGroup
                f'16 ]
                r4
                g'16 [
                af'16 \stopGroup
                r8 ]
                r2
                {
                    R1 * 5
                }
                c'16 \startGroup [
                f'16
                r8
                g'16
                af'16
                r2
                r8 ]
                {
                    R1 * 1
                }
                c''16 [
                c'16
                r8
                bf16
                ef'16 \stopGroup
                f'16 \startGroup
                g'16
                r4
                bf'16
                bf16 \stopGroup
                c'16 \startGroup
                f'16 ]
                r8 [
                g'16
                af'16
                r2. ]
                {
                    R1 * 1
                }
                c''16 [
                c'16
                r8 ]
                bf16 [
                ef'16 \stopGroup
                f'16 \startGroup
                g'16 ]
                r8 [
                bf'16
                bf16 ]
                r4
                a16 [
                d'16
                r8 ]
                ef'16 [
                f'16 \stopGroup
                c'16 \startGroup
                f'16 ]
                r4
                g'16 [
                af'16 \stopGroup
                c''16 \startGroup
                c'16 ]
                bf16 [
                ef'16 \stopGroup
                f'16 \startGroup
                g'16 ]
                bf'16 [
                bf16 \stopGroup
                a16 \startGroup
                d'16 ]
                r8 [
                ef'16
                f'16 ]
                r4
                r8 [
                af'16
                a16 ]
                r8 [
                g16
                c'16 \stopGroup ]
                c'16 \startGroup [
                f'16
                r8 ]
                g'16 [
                af'16 \stopGroup
                c''16 \startGroup
                c'16 ]
                r8 [
                bf16
                ef'16 \stopGroup ]
                f'16 \startGroup [
                g'16
                bf'16
                bf16 \stopGroup ]
                a16 \startGroup [
                d'16
                r8 ]
                r8 [
                ef'16
                f'16 \stopGroup ]
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                \accidentalStyle modern-cautionary
                c'16 \startGroup [
                f'16
                r8 ]
                g'16 [
                af'16
                r8 ]
                r2
                {
                    R1 * 2
                }
                r2
                r8 [
                c''16
                c'16 ]
                r8 [
                bf16
                ef'16 \stopGroup ]
                f'16 \startGroup [
                g'16
                r8 ]
                bf'16 [
                bf16
                r8 ]
                r2
                {
                    R1 * 1
                }
                r2 [
                r8
                a16
                d'16
                r8
                ef'16
                f'16 \stopGroup ]
                g'16 \startGroup [
                c''16
                r8
                d''16
                ef''16
                r2
                r8 ]
                {
                    R1 * 1
                }
                r2 [
                r8
                g'16
                g'16
                r8
                f'16
                bf'16 \stopGroup ]
                c''16 \startGroup [
                d''16
                r8
                f'16
                f'16
                r2
                r8 ]
                r2 [
                r8
                e''16
                a'16
                r8
                bf'16
                c''16 \stopGroup ]
                bf'16 \startGroup [
                ef''16
                r8
                f'16
                fs'16
                r2
                r8 ]
                {
                    R1 * 1
                }
                r2 [
                r8
                bf'16
                bf'16
                r8
                af'16
                cs''16 \stopGroup ]
                ef''16 \startGroup [
                f'16
                r8
                af'16
                af'16
                r2
                r8 ]
                r2 [
                r8
                g'16
                c''16
                r8
                cs''16
                ef''16 \stopGroup ]
                c''16 \startGroup [
                f''16
                r8
                g''16
                af''16
                r2
                r8 ]
                r8 [
                c''16
                c''16
                r8
                bf'16
                ef''16 \stopGroup
                d''16 \startGroup
                c'''16
                r8
                f''16
                g''16
                r8 ]
                r8 [
                af''16
                c'''16
                r8
                c'''16
                bf''16 \stopGroup
                ef''16 \startGroup
                f''16
                r4
                g''16
                bf''16 \stopGroup ]
            }
        }
        \context Staff = "Cello" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Vc. }
            \clef "bass"
            {
                \accidentalStyle modern-cautionary
                c'1
            }
        }
    >>
}