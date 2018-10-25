% 2018-07-11 22:53

\version "2.18.2"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "SlowRhythm" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { SlowRhythm }
            \set Staff.shortInstrumentName = \markup { SlowRhythm }
            {
                c'4
                c'2
                c'4 ~
                c'2
                c'2 ~
                c'2
                c'2 ~
                c'4
                c'2
                c'4
                c'4
                c'2
                c'4 ~
                c'2
                c'2 ~
                c'2
                c'2 ~
                c'4
                c'2
                c'4
                c'4
                c'2
                c'4 ~
                c'2
                c'2 ~
                c'4
                c'2
                c'4
                c'4
                c'2
                c'4 ~
                c'2
                c'2 ~
                c'4
                c'2
                c'4
            }
        }
        \context Staff = "c" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { C }
            \set Staff.shortInstrumentName = \markup { C }
            {
                d'4
                ef'4
                f'2
            }
        }
        \context Staff = "p" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { P }
            \set Staff.shortInstrumentName = \markup { P }
            {
                d'4 -\accent -\staccato
                ef'4 -\accent -\staccato
                f'2 -\accent -\staccato
                d'4
                ef'4
                f'2
                d'4 -\accent -\staccato
                ef'4
                f'2
            }
        }
    >>
}