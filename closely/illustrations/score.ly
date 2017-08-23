% 2017-08-22 16:44

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
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
            }
        }
        \context Staff = "Clarinet" {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
            }
        }
        \context Staff = "Violin" {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
            }
        }
        \context Staff = "Cello" {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Vc. }
            \clef "bass"
            {
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
                {
                    \accidentalStyle modern-cautionary
                    c'1
                }
            }
        }
    >>
}