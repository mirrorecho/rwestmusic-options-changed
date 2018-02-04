% 2017-12-05 22:17

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Event1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Event1 }
            \set Staff.shortInstrumentName = \markup { Event1 }
            {
                d'4
                r2.
            }
        }
        \context Staff = "Event2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Event2 }
            \set Staff.shortInstrumentName = \markup { Event2 }
            {
                f'8 [
                r2.. ]
            }
        }
        \context Staff = "Event3" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Event3 }
            \set Staff.shortInstrumentName = \markup { Event3 }
            {
                e'8 [
                r2.. ]
            }
        }
        \context Staff = "Event4" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Event4 }
            \set Staff.shortInstrumentName = \markup { Event4 }
            {
                g'4
                r2.
            }
        }
        \context Staff = "Event5" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Event5 }
            \set Staff.shortInstrumentName = \markup { Event5 }
            {
                af'4
                r2.
            }
        }
    >>
}