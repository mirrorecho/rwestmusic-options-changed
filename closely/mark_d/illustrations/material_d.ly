% 2017-09-20 00:11

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "line_0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line_0 }
            \set Staff.shortInstrumentName = \markup { Line_0 }
            {
                \accidentalStyle modern-cautionary
                r8
                c'4.
                c'2 ~
                c'8
                c'4
                c'4.
                c'4 ~
                c'4.
                c'8 [
                r8 ]
                c'4.
                c'2.
                c'4 ~
                c'4.
                c'8 [
                r2 ]
            }
        }
        \context Staff = "line_1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line_1 }
            \set Staff.shortInstrumentName = \markup { Line_1 }
            {
                \accidentalStyle modern-cautionary
                r8
                c'4.
                c'2 ~
                c'8
                c'4
                c'4.
                c'4 ~
                c'4.
                c'8 [
                r8 ]
                c'4.
                c'2.
                c'4 ~
                c'4.
                c'8 [
                r2 ]
            }
        }
        \context Staff = "line_2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line_2 }
            \set Staff.shortInstrumentName = \markup { Line_2 }
            {
                \accidentalStyle modern-cautionary
                r2 [
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
                c'8 [
                c'8
                r2 ]
                c'8 [
                c'8 ]
                c'4
                c'4
                c'4
                c'4
                c'8 [
                c'8
                r2 ]
            }
        }
    >>
}