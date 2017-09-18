% 2017-09-17 21:56

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
                c'4.
                c'8 ~
                c'8 [
                c'8 ]
                c'4
                c'4.
                c'8
                c'4
                c'4 ~
                c'8
                c'4
                c'8
                c'4
                c'4 ~
                c'8
                c'4
                c'8 ~
                c'8
                c'4
                c'8
                c'4
                r4
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
                c'8 [
                c'8 ]
                c'4
                c'4
                c'8 [
                c'8 ]
                c'8 [
                c'8 ]
                c'4
                c'8 [
                c'8
                c'8
                c'8 ]
                c'4
                c'4
                c'8 [
                c'8
                c'8
                c'8 ]
                c'4
                c'4
                c'4
                c'4
                c'8 [
                c'8
                r4 ]
                r2
                {
                    R1 * 1
                }
            }
        }
    >>
}