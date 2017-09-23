% 2017-09-22 18:55

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
                r8
                gf''4. \startGroup
                cf'''2 ~
                cf'''8
                cf'''4
                cf'''8 ~
                cf'''4
                bff''4 ~
                bff''4.
                g''8 \stopGroup
                r8
                cf'''4. \startGroup
                c'''2 ~
                c'''4
                cf'''4 ~
                cf'''4.
                cf'''8 \stopGroup
                cf''4 \startGroup
                df''4
                cf''8 [
                ef''8 ]
                af''4
                gf''4 \stopGroup
                gf''4 \startGroup
                ff''4
                ef''8 [
                bff''8 ]
                bff''8 [
                cf'''8
                c'''8
                g''8 ]
                cf''4
                cf''4 \stopGroup
                r8
                c'4. \startGroup
                d'2 ~
                d'8
                ef'4
                f'8 ~
                f'4
                g'4 ~
                g'4.
                af'8 \stopGroup
                r8
                bf'4. \startGroup
                c''2 ~
                c''4
                cs''4 ~
                cs''4.
                ef''8 \stopGroup
                r8
                c'4. \startGroup
                d'2 ~
                d'8
                ef'4
                f'8 ~
                f'4
                g'4 ~
                g'4.
                af'8 \stopGroup
                r8
                bf'4. \startGroup
                c''2 ~
                c''4
                cs''4 ~
                cs''4.
                ef''8 \stopGroup
                cf''4 \startGroup
                df''4
                cf''8 [
                ef''8 ]
                af''4
                gf''4 \stopGroup
                gf''4 \startGroup
                ff''4
                ef''8 [
                bff''8 ]
                bff''8 [
                cf'''8
                c'''8
                g''8 ]
                cf''4
                cf''4 \stopGroup
                r2
                {
                    R1 * 10
                }
            }
        }
        \context Staff = "Clarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                \accidentalStyle modern-cautionary
                r8
                cf''4. \startGroup
                ef'2 ~
                ef'8
                gf'4
                cf''8 ~
                cf''4
                cf''4 ~
                cf''4.
                bff'8 \stopGroup
                r8
                gf'4. \startGroup
                g'2 ~
                g'4
                g'4 ~
                g'4.
                gf'8 \stopGroup
                bf'4 \startGroup
                bf'4
                bf'8 [
                cf''8 ]
                cf''4
                df''4 \stopGroup
                ef''4 \startGroup
                gf'4
                cf''8 [
                cf''8 ]
                cf''8 [
                cf''8
                cf''8
                cf''8 ]
                df''4
                cf''4 \stopGroup
                r8
                c'4. \startGroup
                d'2 ~
                d'8
                ef'4
                f'8 ~
                f'4
                g'4 ~
                g'4.
                af'8 \stopGroup
                r8
                bf'4. \startGroup
                c''2 ~
                c''4
                cs''4 ~
                cs''4.
                ef''8 \stopGroup
                r8
                c'4. \startGroup
                d'2 ~
                d'8
                ef'4
                f'8 ~
                f'4
                g'4 ~
                g'4.
                af'8 \stopGroup
                r8
                bf'4. \startGroup
                c''2 ~
                c''4
                cs''4 ~
                cs''4.
                ef''8 \stopGroup
                bf'4 \startGroup
                bf'4
                bf'8 [
                cf''8 ]
                cf''4
                df''4 \stopGroup
                ef''4 \startGroup
                gf'4
                cf''8 [
                cf''8 ]
                cf''8 [
                cf''8
                cf''8
                cf''8 ]
                df''4
                cf''4 \stopGroup
                r2
                {
                    R1 * 10
                }
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                \accidentalStyle modern-cautionary
                r8
                df'4. \startGroup
                gf'2 ~
                gf'8
                ff'4
                af'8 ~
                af'4
                d'4 ~
                d'4.
                d'8 \stopGroup
                r8
                d'4. \startGroup
                d'2 ~
                d'4
                cf'4 ~
                cf'4.
                cf'8 \stopGroup
                f'4 \startGroup
                gf'4
                ef'8 [
                gf'8 ]
                gf'4
                cf'4 \stopGroup
                bf'4 \startGroup
                cf'4
                af8 [
                ff'8 ]
                d'8 [
                d'8
                g'8
                cf'8 ]
                gf'4
                gf'4 \stopGroup
                r2
                c'8 \startGroup [
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8 \stopGroup ]
                bf'8 \startGroup [
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8 \stopGroup ]
                r2
                af''8 \startGroup [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8 \stopGroup ]
                r2
                c'8 \startGroup [
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8 \stopGroup ]
                bf'8 \startGroup [
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8 \stopGroup ]
                r2
                af''8 \startGroup [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8 \stopGroup ]
                f'4 \startGroup
                gf'4
                ef'8 [
                gf'8 ]
                gf'4
                cf'4 \stopGroup
                bf'4 \startGroup
                cf'4
                af8 [
                ff'8 ]
                d'8 [
                d'8
                g'8
                cf'8 ]
                gf'4
                gf'4 \stopGroup
                r2
                {
                    R1 * 10
                }
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
                r8
                cf'4. \startGroup
                bf2 ~
                bf8
                cf'4
                ef'8 ~
                ef'4
                ff'4 ~
                ff'4.
                cf'8 \stopGroup
                r8
                cf'4. \startGroup
                cf'2 ~
                cf'4
                ff'4 ~
                ff'4.
                df'8 \stopGroup
                ef4 \startGroup
                cf4
                af8 [
                cf'8 ]
                df'4
                cf'4 \stopGroup
                cf'4 \startGroup
                cf4
                cf8 [
                d8 ]
                g8 [
                gf8
                d8
                ff8 ]
                cf'4
                ff'4 \stopGroup
                r2
                c'8 \startGroup [
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8 \stopGroup ]
                bf'8 \startGroup [
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8 \stopGroup ]
                r2
                af''8 \startGroup [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8 \stopGroup ]
                r2
                c'8 \startGroup [
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8 \stopGroup ]
                bf'8 \startGroup [
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8 \stopGroup ]
                r2
                af''8 \startGroup [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8 \stopGroup ]
                ef4 \startGroup
                cf4
                af8 [
                cf'8 ]
                df'4
                cf'4 \stopGroup
                cf'4 \startGroup
                cf4
                cf8 [
                d8 ]
                g8 [
                gf8
                d8
                ff8 ]
                cf'4
                ff'4 \stopGroup
                r2
                {
                    R1 * 10
                }
            }
        }
    >>
}