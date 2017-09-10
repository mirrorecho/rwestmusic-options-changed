% 2017-08-28 18:52

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "line_c_0" {
            \set Staff.instrumentName = \markup { Line_c_0 }
            \set Staff.shortInstrumentName = \markup { Line_c_0 }
            {
                c'4
                d'4
                ef'4
                ef'4
                f'4
                g'4
                af'4
                af'4
                af'4
                af'4
                g'4
                f'4
                ef'4
                ef'4
                d'4
                c'4
            }
        }
        \context Staff = "line_c_1" {
            \set Staff.instrumentName = \markup { Line_c_1 }
            \set Staff.shortInstrumentName = \markup { Line_c_1 }
            {
                f'4
                f'4
                af'4
                g'4
                bf'4
                bf'4
                df''4
                c''4
                c''4
                df''4
                bf'4
                bf'4
                g'4
                af'4
                f'4
                f'4
            }
        }
        \context Staff = "line_c_2" {
            \set Staff.instrumentName = \markup { Line_c_2 }
            \set Staff.shortInstrumentName = \markup { Line_c_2 }
            {
                bf'4
                a'4
                df''4
                bf'4
                ef''4
                d''4
                gf''4
                ef''4
                ef''4
                gf''4
                d''4
                ef''4
                bf'4
                df''4
                a'4
                bf'4
            }
        }
        \context Staff = "line_c_3" {
            \set Staff.instrumentName = \markup { Line_c_3 }
            \set Staff.shortInstrumentName = \markup { Line_c_3 }
            {
                c''4
                d''4
                ef''4
                ef''4
                f''4
                g''4
                af''4
                af''4
                af''4
                af''4
                g''4
                f''4
                ef''4
                ef''4
                d''4
                c''4
            }
        }
        \context Staff = "Noneconstant_pitch_-12" {
            \set Staff.instrumentName = \markup { Noneconstant_pitch_-12 }
            \set Staff.shortInstrumentName = \markup { Noneconstant_pitch_-12 }
            {
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
                c4
            }
        }
    >>
}