% 2017-12-05 00:11

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
                r8 [
                d'8
                d'8
                d'8 ] \startGroup
                e'8 [
                e'8
                e'8
                e'8 ]
                e'8 [
                g'8
                g'8
                a'8 ]
                a'8 [
                a'8
                f'8
                f'8 ]
                f'8 [
                f'8
                f'8
                bf'8 \stopGroup ]
                r8
                c''4. \startGroup
                ef''2 ~
                ef''4
                f''4 ~
                f''4.
                d''8 \stopGroup
                r2
                {
                    R1 * 27
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
                r8 [
                g'8
                g'8
                g'8 ] \startGroup
                g'8 [
                g'8
                g'8
                g'8 ]
                g'8 [
                c''8
                c''8
                c''8 ]
                c''8 [
                c''8
                bf'8
                bf'8 ]
                bf'8 [
                bf'8
                bf'8
                ef''8 \stopGroup ]
                r8
                ef''4. \startGroup
                af''2 ~
                af''4
                af''4 ~
                af''4.
                g''8 \stopGroup
                r2
                {
                    R1 * 27
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
                r8 [
                c''8
                c''8
                c''8 ] \startGroup
                b'8 [
                b'8
                b'8
                b'8 ]
                b'8 [
                f''8
                f''8
                e''8 ]
                e''8 [
                e''8
                ef''8
                ef''8 ]
                ef''8 [
                ef''8
                ef''8
                af''8 \stopGroup ]
                r8
                g''4. \startGroup
                df'''2 ~
                df'''4
                c'''4 ~
                c'''4.
                c'''8 \stopGroup
                r2
                {
                    R1 * 27
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
                r8 [
                c'8
                c'8
                c'8 ] \startGroup
                c'8 [
                c'8
                c'8
                c'8 ]
                c'8 [
                c'8
                c'8
                c'8 ]
                c'8 [
                c'8
                c'8
                c'8 ]
                c'8 [
                c'8
                c'8
                c'8 \stopGroup ]
                r8
                c'4. \startGroup
                c'2 ~
                c'4
                c'4 ~
                c'4.
                c'8 \stopGroup
                r2
                {
                    R1 * 27
                }
            }
        }
    >>
    \midi {}
}