% 2017-08-11 12:00

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "my_line1_0" {
            \set Staff.instrumentName = \markup { My_line1_0 }
            \set Staff.shortInstrumentName = \markup { My_line1_0 }
            {
                {
                    \accidentalStyle modern-cautionary
                    d''4
                    f'8 [
                    e'8 ]
                    g'4
                    r4
                    af'4
                    r2.
                }
            }
        }
        \context Staff = "my_line1_1" {
            \set Staff.instrumentName = \markup { My_line1_1 }
            \set Staff.shortInstrumentName = \markup { My_line1_1 }
            {
                {
                    \accidentalStyle modern-cautionary
                    a'4
                    g'8 [
                    fs'8 ]
                    a'4
                    r4
                    bf'4
                    r2.
                }
            }
        }
        \context Staff = "my_line1_2" {
            \set Staff.instrumentName = \markup { My_line1_2 }
            \set Staff.shortInstrumentName = \markup { My_line1_2 }
            {
                {
                    \accidentalStyle modern-cautionary
                    f'4
                    c''8 [
                    g'8 ]
                    d''4
                    r4
                    ef''4
                    r2.
                }
            }
        }
        \context Staff = "my_line1_3" {
            \set Staff.instrumentName = \markup { My_line1_3 }
            \set Staff.shortInstrumentName = \markup { My_line1_3 }
            {
                {
                    \accidentalStyle modern-cautionary
                    e'4
                    d''8 [
                    b'8 ]
                    e''4
                    r4
                    f''4
                    r2.
                }
            }
        }
        \context Staff = "my_line1_4" {
            \set Staff.instrumentName = \markup { My_line1_4 }
            \set Staff.shortInstrumentName = \markup { My_line1_4 }
            {
                {
                    \accidentalStyle modern-cautionary
                    d'4
                    f''8 [
                    e''8 ]
                    g''4
                    r4
                    af''4
                    r2.
                }
            }
        }
    >>
}