% 2017-09-17 21:27

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
                df''4. \startGroup
                ef''2 ~
                ef''8
                ff''4
                cf''8 ~
                cf''4
                d''4 ~
                d''4.
                cf''8 \stopGroup
                r8
                cf''4. \startGroup
                d''2 ~
                d''4
                cf''4 ~
                cf''4.
                gf''8 \stopGroup
                r2
                {
                    R1 * 25
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
                gf'4. \startGroup
                gf'2 ~
                gf'8
                gf'4
                cf''8 ~
                cf''4
                bff'4 ~
                bff'4.
                g'8 \stopGroup
                r8
                cf''4. \startGroup
                c''2 ~
                c''4
                cf''4 ~
                cf''4.
                df''8 \stopGroup
                r2
                {
                    R1 * 25
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
                cf'4. \startGroup
                bf2 ~
                bf8
                cf'4
                ef'8 ~
                ef'4
                cf'4 ~
                cf'4.
                bff8 \stopGroup
                r8
                gf'4. \startGroup
                g'2 ~
                g'4
                ff'4 ~
                ff'4.
                cf''8 \stopGroup
                r2
                {
                    R1 * 25
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
                cf4. \startGroup
                cf'2 ~
                cf'8
                cf'4
                af8 ~
                af4
                ff'4 ~
                ff'4.
                d'8 \stopGroup
                r8
                d4. \startGroup
                cf2 ~
                cf4
                g4 ~
                g4.
                cf8 \stopGroup
                r2
                {
                    R1 * 25
                }
            }
        }
    >>
}