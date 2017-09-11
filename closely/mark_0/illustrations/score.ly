% 2017-09-11 01:43

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
                {
                    R1 * 2
                }
                e''4 \pp
                a''2
                fs''4 ~
                fs''2
                a''2 ~
                a''4
                d''2
                bf''4
                e''4
                c''2
                ef''4 ~
                ef''2
                a''2 ~
                a''4
                f''2
                bf''4
                {
                    R1 * 4
                }
                fs''8 [
                d''8 ]
                f''4
                d''4
                f''4
                b''4
                f''8 [
                b''8
                g''8
                b''8 ]
                g''4
                c''4
                g''8 [
                c''8
                a''8
                c''8 ]
                a''4
                c''4
                a''8 [
                c''8
                f''8
                c''8
                f''8
                d''8 ]
                f''8 [
                d''8 ]
                g''4
                d''4
                g''8 [
                e''8 ]
                g''8 [
                e''8
                g''8
                e''8
                g''8
                c''8 ]
                g''4
                c''4
                af''8 [
                c''8
                af''8
                d''8 ]
                af''4
                d''4
                bf''8 [
                d''8
                bf''8
                cs'''8
                bf''8
                cs'''8 ]
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
                    R1 * 2
                }
                e'4 \pp
                f'2
                a4 ~
                a2
                b2 ~
                b4
                fs2
                g'4
                a'4
                c'2
                d'4 ~
                d'2
                a2 ~
                a4
                bf'2
                c''4
                {
                    R1 * 4
                }
                g8 [
                e'8 ]
                a4
                e'4
                a4
                fs4
                a8 [
                fs8
                a'8
                fs8 ]
                a'4
                d'4
                a'8 [
                d'8
                bf'8
                d'8 ]
                bf'4
                e'4
                bf'8 [
                e'8
                c'8
                e'8
                c'8
                ef''8 ]
                c'8 [
                ef''8 ]
                a'4
                ef''4
                a'8 [
                f''8 ]
                a'8 [
                f''8
                bf'8
                f''8
                bf'8
                g'8 ]
                bf'4
                g'4
                bf''8 [
                g'8
                bf''8
                ef''8 ]
                bf''4
                ef''4
                c'''8 [
                ef''8
                c'''8
                f''8
                c'''8
                f''8 ]
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                \accidentalStyle modern-cautionary
                {
                    R1 * 2
                }
                f'4 \pp ^ \markup { "sul. pont" }
                b2
                g'4 ~
                g'2
                c'2 ~
                c'4
                a2
                c'4
                f'4
                d'2
                g'4 ~
                g'2
                e'2 ~
                e'4
                g'2
                c'4
                {
                    R1 * 4
                }
                d'8 [
                e'8 ]
                f'4
                a4
                b4
                fs'4
                g'8 [
                a'8
                c'8
                d'8 ]
                a4
                bf'4
                c''8 [
                e'8
                f'8
                c'8 ]
                d''4
                ef''4
                r2
                g'4
                a'4
                e'8 [
                f''8
                g''8
                bf'8 ]
                c''4
                g'4
                af''4
                bf''4
                d''8 [
                ef''8 ]
                bf'8 [
                c'''8 ]
                cs''4
                f''4
                g''8 [
                d''8 ]
                ef''8 [
                f''8 ]
                af''4
                bf''4
                f''8 [
                fs''8 ]
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
                e4 \pp ^ \markup { "sul. pont" }
                e2
                e4 ~
                e2
                e2 ~
                e2
                e2 ~
                e2
                e2 ~
                e4
                e2
                e4
                e4
                e2
                e4 ~
                e2
                e2 ~
                e2
                e2 ~
                e2
                e2 ~
                e4
                e2
                e4
                e8 [
                e8 ]
                e4
                e4
                r4
                r4
                e4
                e4
                e8 [
                e8 ]
                e8 [
                e8 ]
                e4
                e4
                e4
                e4
                e8 [
                e8
                e8 \<
                e8 ]
                e4
                e4
                e8 [
                e8
                a8 \mp
                a8 ]
                a4
                a4
                r2
                a4
                a4
                a8 [
                a8
                a8
                a8 ]
                a4
                a4
                a4
                a4
                a8 [
                a8 ]
                a8 [
                a8 ]
                a4
                a4
                a8 [
                a8 ]
                a8 [
                a8 ]
                a4
                a4
                a8 [
                a8 ]
            }
        }
    >>
}