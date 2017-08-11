% 2017-08-10 16:42

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Flute" {
            \set Staff.instrumentName = \markup { Flute }
            \set Staff.shortInstrumentName = \markup { Fl. }
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
        \context Staff = "Clarinet" {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                \accidentalStyle modern-cautionary
                r2
                d'16 [ (
                e'16
                f'16
                g'16 )
                af'8 ]
                r8
                g'16 [ (
                af'16
                a'16 )
                bf'8 ]
                r2
                r8.
            }
        }
        \context Staff = "Violin" {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
        }
        \context Staff = "Cello" {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Vc. }
            \clef "bass"
        }
    >>
}