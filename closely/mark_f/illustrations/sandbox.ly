% 2017-09-13 14:55

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "LineA" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { LineA }
            \set Staff.shortInstrumentName = \markup { LineA }
            {
                \accidentalStyle modern-cautionary
                c'4
                r8 [
                c'8
                r8
                c'8
                r8
                c'8 ]
                r8 [
                c'8 ]
                c'4
                c'4
                r8 [
                c'8 ]
                r8 [
                c'8
                r8
                c'8
                r8
                c'8 ]
                c'4
                c'4.
                c'4
                c'4
                c'8 ~
                c'8 [
                c'8 ]
                c'4
                c'4.
                c'8 ~
                c'8
                c'4
                c'4
                c'8
                c'4
            }
        }
    >>
}