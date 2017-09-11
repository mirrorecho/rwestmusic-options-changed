% 2017-09-10 18:43

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Flute" {
            \set Staff.instrumentName = \markup { Flute }
            \set Staff.shortInstrumentName = \markup { Flute }
            {
                \accidentalStyle modern-cautionary
                c'1
            }
        }
        \context Staff = "Clarinet" {
            \set Staff.instrumentName = \markup { Clarinet }
            \set Staff.shortInstrumentName = \markup { Clarinet }
            {
                \accidentalStyle modern-cautionary
                c'1
            }
        }
        \context Staff = "Violin" {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Violin }
            {
                \accidentalStyle modern-cautionary
                c'16 [
                f'16 ]
                r8
                g'16 [
                af'16 ]
                r2
                r8
                r1
                r1
                r2
                r8
                c''16 [
                c'16 ]
                r8
                bf16 [
                ef'16 ]
                f'16 [
                g'16 ]
                r8
                bf'16 [
                bf16 ]
                r2
                r8
                r1
                r2
                r8
                a16 [
                d'16 ]
                r8
                ef'16 [
                f'16 ]
                g'16 [
                c''16 ]
                r8
                d''16 [
                ef''16 ]
                r2
                r8
                r1
                r2
                r8
                g'16 [
                g'16 ]
                r8
                f'16 [
                bf'16 ]
                c''16 [
                d''16 ]
                r8
                f'16 [
                f'16 ]
                r2
                r8
                r2
                r8
                e''16 [
                a'16 ]
                r8
                bf'16 [
                c''16 ]
                bf'16 [
                ef''16 ]
                r8
                f'16 [
                fs'16 ]
                r2
                r8
                r1
                r2
                r8
                bf'16 [
                bf'16 ]
                r8
                af'16 [
                cs''16 ]
                ef''16 [
                f'16 ]
                r8
                af'16 [
                af'16 ]
                r2
                r8
                r2
                r8
                g'16 [
                c''16 ]
                r8
                cs''16 [
                ef''16 ]
                c''16 [
                f''16 ]
                r8
                g''16 [
                af''16 ]
                r2
                r8
                r8
                c''16 [
                c''16 ]
                r8
                bf'16 [
                ef''16
                d''16
                c'''16 ]
                r8
                f''16 [
                g''16 ]
                r8
                r8
                af''16 [
                c'''16 ]
                r8
                c'''16 [
                bf''16
                ef''16
                f''16 ]
                r4
                g''16 [
                bf''16 ]
            }
        }
        \context Staff = "Cello" {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Cello }
            {
                \accidentalStyle modern-cautionary
                c'1
            }
        }
    >>
}