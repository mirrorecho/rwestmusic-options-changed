% 2017-08-11 12:00

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "CloselyCell" {
            \set Staff.instrumentName = \markup { CloselyCell }
            \set Staff.shortInstrumentName = \markup { CloselyCell }
            {
                \accidentalStyle modern-cautionary
                d'4
                f'8 [
                e'8 ]
                g'4
                r4
                af'4
                r2.
            }
        }
        \context Staff = "CloselyCellTr2" {
            \set Staff.instrumentName = \markup { CloselyCellTr2 }
            \set Staff.shortInstrumentName = \markup { CloselyCellTr2 }
            {
                \accidentalStyle modern-cautionary
                e'4
                g'8 [
                fs'8 ]
                a'4
                r4
                bf'4
                r2.
            }
        }
        \context Staff = "CloselyCellDisplaced" {
            \set Staff.instrumentName = \markup { CloselyCellDisplaced }
            \set Staff.shortInstrumentName = \markup { CloselyCellDisplaced }
            {
                \accidentalStyle modern-cautionary
                a'4
                bf'8 [
                e'8 ]
                g'4
                r4
                af'4
                r2.
            }
        }
        \context Staff = "UpLick" {
            \set Staff.instrumentName = \markup { UpLick }
            \set Staff.shortInstrumentName = \markup { UpLick }
            {
                \accidentalStyle modern-cautionary
                r16
                d'16 [
                e'16
                f'16 ]
                g'2
                af'4
            }
        }
        \context Staff = "UpLickDisplaced" {
            \set Staff.instrumentName = \markup { UpLickDisplaced }
            \set Staff.shortInstrumentName = \markup { UpLickDisplaced }
            {
                \accidentalStyle modern-cautionary
                e'16 [ (
                g'16
                af'16 ]
                a'2 )
                bf'8
                r8.
            }
        }
    >>
}