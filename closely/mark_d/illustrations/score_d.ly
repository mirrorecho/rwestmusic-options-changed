% 2017-12-05 00:10

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
                d'4. \startGroup
                f'8 ~
                f'8
                g'4
                e'8
                a'4 \stopGroup
                bf'4 ~ \startGroup
                bf'8
                d''4
                ef''8 ~
                ef''8 [
                c''8 ]
                f''4 \stopGroup
                r2
                {
                    R1 * 29
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
                f'4. \startGroup
                bf'8 ~
                bf'8
                bf'4
                a'8
                d''4 \stopGroup
                d''4 ~ \startGroup
                d''8
                g''4
                g''8 ~
                g''8 [
                f''8 ]
                bf''4 \stopGroup
                r2
                {
                    R1 * 29
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
                a'4. \startGroup
                ef''8 ~
                ef''8
                d''4
                d''8
                g''4 \stopGroup
                f''4 ~ \startGroup
                f''8
                c'''4
                bf''8 ~
                bf''8 [
                bf''8 ]
                ef'''4 \stopGroup
                r2
                {
                    R1 * 29
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
                d'4. \startGroup
                d'8 ~
                d'8
                d'4
                d'8
                d'4 \stopGroup
                d'4 ~ \startGroup
                d'8
                d'4
                d'8 ~
                d'8 [
                d'8 ]
                d'4 \stopGroup
                r2
                {
                    R1 * 29
                }
            }
        }
    >>
    \midi {}
}