% 2018-05-08 23:47

\version "2.19.54"
\language "english"

\include "../../stylesheets/score.ily"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Violin1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Violin 1" }
            \set Staff.shortInstrumentName = \markup { Vln.1 }
        }
        \context Staff = "Violin2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Violin 2" }
            \set Staff.shortInstrumentName = \markup { Vln.2 }
        }
        \context Staff = "Viola" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Viola }
            \set Staff.shortInstrumentName = \markup { Vla. }
            {
                \accidentalStyle modern-cautionary
                {
                    R1 * 2
                }
                f'4 \pp \startGroup ^ \markup { "sul. pont" }
                b2
                g4 ~
                g2
                c'2 ~
                c'4
                a2
                c'4 \stopGroup
                f'4 \startGroup
                d'2
                g'4 \stopGroup
                e'4 \startGroup
                g'2
                c''4 \stopGroup
                af'4 \startGroup
                d'2
                bf4 \stopGroup
                {
                    R1 * 4
                }
                d'8 \startGroup [
                e'8 ]
                f'4
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
        }
    >>
    \midi {}
}