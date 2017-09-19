% 2017-09-19 01:44

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Line1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line1 }
            \set Staff.shortInstrumentName = \markup { Line1 }
            {
                \accidentalStyle modern-cautionary
                r8
                c'4. \startGroup
                c'2 ~
                c'8
                c'4
                c'8 ~
                c'4
                c'4 ~
                c'4.
                c'8 \stopGroup
                r8
                c'4. \startGroup
                c'2 ~
                c'4
                c'4 ~
                c'4.
                c'8 \stopGroup
                r2
                {
                    R1 * 1
                }
            }
        }
        \context Staff = "Line2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line2 }
            \set Staff.shortInstrumentName = \markup { Line2 }
            {
                \accidentalStyle modern-cautionary
                r2
                c'8 \startGroup [
                c'8 ]
                c'4
                c'4
                c'8 [
                c'8 \stopGroup ]
                c'8 \startGroup [
                c'8 ]
                c'4
                c'4
                c'8 [
                c'8 \stopGroup ]
                r2
                c'8 \startGroup [
                c'8 ]
                c'4
                c'4
                c'4
                c'4
                c'8 [
                c'8 \stopGroup ]
                r2
                {
                    R1 * 1
                }
            }
        }
    >>
}