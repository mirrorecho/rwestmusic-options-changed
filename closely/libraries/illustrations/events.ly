% 2017-08-10 21:59

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Event1" {
            \set Staff.instrumentName = \markup { Event1 }
            \set Staff.shortInstrumentName = \markup { Event1 }
            {
                \accidentalStyle modern-cautionary
                d'4
                r2.
            }
        }
        \context Staff = "Event2" {
            \set Staff.instrumentName = \markup { Event2 }
            \set Staff.shortInstrumentName = \markup { Event2 }
            {
                \accidentalStyle modern-cautionary
                f'8
                r2..
            }
        }
        \context Staff = "Event3" {
            \set Staff.instrumentName = \markup { Event3 }
            \set Staff.shortInstrumentName = \markup { Event3 }
            {
                \accidentalStyle modern-cautionary
                e'8
                r2..
            }
        }
        \context Staff = "Event4" {
            \set Staff.instrumentName = \markup { Event4 }
            \set Staff.shortInstrumentName = \markup { Event4 }
            {
                \accidentalStyle modern-cautionary
                g'4
                r2.
            }
        }
        \context Staff = "Event5" {
            \set Staff.instrumentName = \markup { Event5 }
            \set Staff.shortInstrumentName = \markup { Event5 }
            {
                \accidentalStyle modern-cautionary
                af'4
                r2.
            }
        }
    >>
}