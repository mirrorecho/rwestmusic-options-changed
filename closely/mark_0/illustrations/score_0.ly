% 2018-01-27 17:00

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
                e'4 \pp \startGroup
                a'2
                fs'4 ~
                fs'2
                a'2 ~
                a'4
                d''2
                bf'4 \stopGroup
                e'4 \startGroup
                c''2
                ef''4 \stopGroup
                a'4 \startGroup
                f'2
                bf'4 \stopGroup
                g'4 \startGroup
                bf'2
                ef''4 \stopGroup
                {
                    R1 * 4
                }
                fs''8 \startGroup [
                d''8 ]
                f''4
                d''4
                f''4
                b'4
                f'8 [
                b'8 \stopGroup
                g'8 \startGroup
                b'8 ]
                g'4
                c''4
                g'8 [
                c''8 \stopGroup
                a'8 \startGroup
                c''8 ]
                a'4
                c''4
                a'8 [
                c''8 \stopGroup
                f''8 \startGroup
                c''8
                f''8
                d''8 \stopGroup ]
                f''8 \startGroup [
                d''8 ]
                g''4
                d''4
                g''8 [
                e''8 \stopGroup ]
                g''8 \startGroup [
                e''8
                g''8
                e''8 \stopGroup
                g''8 \startGroup
                c'''8 ]
                g''4
                c'''4
                af''8 [
                c'''8 \stopGroup
                af''8 \startGroup
                d''8 ]
                af'4
                d''4
                bf'8 [
                d''8 \stopGroup
                bf'8 \startGroup
                cs''8
                bf'8
                cs''8 \stopGroup ]
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
                e'4 \pp \startGroup
                f'2
                a'4 ~
                a'2
                b'2 ~
                b'4
                fs'2
                g'4 \stopGroup
                a'4 \startGroup
                c''2
                d''4 ~
                d''2
                a'2 ~
                a'4
                bf'2
                c''4 \stopGroup
                {
                    R1 * 4
                }
                g'8 \startGroup [
                e'8 ]
                a'4
                e'4
                a'4
                fs'4
                a'8 [
                fs'8 \stopGroup
                a'8 \startGroup
                fs'8 ]
                a'4
                d''4
                a'8 [
                d''8 \stopGroup
                bf'8 \startGroup
                d''8 ]
                bf'4
                e'4
                bf8 [
                e'8 \stopGroup
                c'8 \startGroup
                e'8
                c'8
                ef'8 \stopGroup ]
                c'8 \startGroup [
                ef'8 ]
                a4
                ef'4
                a8 [
                f'8 \stopGroup ]
                a'8 \startGroup [
                f'8
                bf'8
                f'8 \stopGroup
                bf'8 \startGroup
                g'8 ]
                bf'4
                g'4
                bf'8 [
                g'8 \stopGroup
                bf'8 \startGroup
                ef''8 ]
                bf'4
                ef''4
                c''8 [
                ef''8 \stopGroup
                c''8 \startGroup
                f''8
                c''8
                f''8 \stopGroup ]
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
                f'4 \pp \startGroup ^ \markup { "sul. pont" }
                g'2
                a'4 ~
                a'2
                f'2 ~
                f'4
                g'2
                g'4 \stopGroup
                af'4 \startGroup
                bf'2
                g'4 \stopGroup
                af'4 \startGroup
                af'2
                bf'4 \stopGroup
                c''4 \startGroup
                af'2
                bf'4 \stopGroup
                {
                    R1 * 4
                }
                d''8 \startGroup [
                e''8 ]
                f''4
                a'4
                b'4
                fs'4
                g'8 [
                a'8 \stopGroup
                c''8 \startGroup
                d''8 ]
                a'4
                bf'4
                c''8 [
                e''8 \stopGroup
                f''8 \startGroup
                c''8 ]
                d''4
                ef''4
                r2
                g''4
                a'4
                e'8 [
                f'8 \stopGroup
                g'8 \startGroup
                bf'8 ]
                c''4
                g'4
                af'4
                bf'4
                d''8 [
                ef''8 \stopGroup ]
                bf'8 \startGroup [
                c''8 ]
                cs''4
                f''4
                g''8 [
                d''8 \stopGroup ]
                ef''8 \startGroup [
                f''8 ]
                af''4
                bf'4
                f'8 [
                fs'8 \stopGroup ]
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
                e4 \pp \startGroup ^ \markup { "sul. pont" }
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
                e4 \stopGroup
                e4 \startGroup
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
                e4 \stopGroup
                e8 \startGroup [
                e8 ]
                e4
                e4
                r4
                r4
                e4
                e4
                e8 [
                e8 \stopGroup ]
                e8 \startGroup [
                e8 ]
                e4
                e4
                e4
                e4
                e8 [
                e8 \stopGroup
                e8 \< \startGroup
                e8 ]
                e4
                e4
                e8 [
                e8 \stopGroup
                a8 \mp \startGroup
                a8 ]
                a4
                a4
                r2
                a4
                a4
                a8 [
                a8 \stopGroup
                a8 \startGroup
                a8 ]
                a4
                a4
                a4
                a4
                a8 [
                a8 \stopGroup ]
                a8 \startGroup [
                a8 ]
                a4
                a4
                a8 [
                a8 \stopGroup ]
                a8 \startGroup [
                a8 ]
                a4
                a4
                a8 [
                a8 \stopGroup ]
            }
        }
    >>
    \midi {}
}