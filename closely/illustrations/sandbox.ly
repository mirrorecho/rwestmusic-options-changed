% 2017-08-09 22:28

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Line1" {
            \set Staff.instrumentName = \markup { Line1 }
            \set Staff.shortInstrumentName = \markup { Line1 }
            {
                \accidentalStyle modern-cautionary
                r1
                r1
                r1
                c1
            }
        }
        \context Staff = "Line2" {
            \set Staff.instrumentName = \markup { Line2 }
            \set Staff.shortInstrumentName = \markup { Line2 }
            {
                \accidentalStyle modern-cautionary
                r1
                r1
                r1
                c1
            }
        }
    >>
}