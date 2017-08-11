% 2017-08-10 16:24

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "LicksPhrase" {
            \set Staff.instrumentName = \markup { LicksPhrase }
            \set Staff.shortInstrumentName = \markup { LicksPhrase }
            {
                \accidentalStyle modern-cautionary
                d'16 [ (
                e'16
                f'16
                g'16 ] )
                af'2
                r16
                g'16 [ (
                af'16
                a'16 ] )
                bf'2
                r2
            }
        }
    >>
}