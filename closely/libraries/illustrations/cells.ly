% 2017-08-18 00:36

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
                d'4
                f'8 [
                e'8 ]
                g'4
                af'4
            }
        }
        \context Staff = "CloselyCellTr2" {
            \set Staff.instrumentName = \markup { CloselyCellTr2 }
            \set Staff.shortInstrumentName = \markup { CloselyCellTr2 }
            {
                e'4
                g'8 [
                fs'8 ]
                a'4
                bf'4
            }
        }
        \context Staff = "CloselyCellDisplaced" {
            \set Staff.instrumentName = \markup { CloselyCellDisplaced }
            \set Staff.shortInstrumentName = \markup { CloselyCellDisplaced }
            {
                a'4
                bf'8 [
                e'8 ]
                g'4
                af'4
            }
        }
        \context Staff = "UpLick" {
            \set Staff.instrumentName = \markup { UpLick }
            \set Staff.shortInstrumentName = \markup { UpLick }
            {
                d'16 [ (
                e'16
                f'16
                g'16 ] )
                af'2
                r4
            }
        }
        \context Staff = "UpLickDisplaced" {
            \set Staff.instrumentName = \markup { UpLickDisplaced }
            \set Staff.shortInstrumentName = \markup { UpLickDisplaced }
            {
                g'16 [ (
                af'16
                a'16 ] )
                bf'2
                r4
                r16
            }
        }
        \context Staff = "CloselyStacked1" {
            \set Staff.instrumentName = \markup { CloselyStacked1 }
            \set Staff.shortInstrumentName = \markup { CloselyStacked1 }
            {
                d'4
                <e' f'>8
                <g' af'>4
                r4.
            }
        }
        \context Staff = "BiggerCell" {
            \set Staff.instrumentName = \markup { BiggerCell }
            \set Staff.shortInstrumentName = \markup { BiggerCell }
            {
                d'4
                f'8 [
                e'8 ]
                g'4
                af'4
                d'4
                f'8 [
                e'8 ]
                g'4
                af'4
                d'4
                f'8 [
                e'8 ]
                g'4
                af'4
                d'4
                f'8 [
                e'8 ]
                g'4
                af'4
            }
        }
    >>
}