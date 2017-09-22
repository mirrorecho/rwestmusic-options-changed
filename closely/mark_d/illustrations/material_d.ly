% 2017-09-21 23:50

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Line0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line0 }
            \set Staff.shortInstrumentName = \markup { Line0 }
            {
                \accidentalStyle modern-cautionary
                r8
                c'4.
                d'2 ~
                d'8
                ef'4
                f'4.
                g'4 ~
                g'4.
                af'8 [
                r8 ]
                bf'4.
                c''2.
                cs''4 ~
                cs''4.
                ef''8 [
                r2 ]
            }
        }
        \context Staff = "Line1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line1 }
            \set Staff.shortInstrumentName = \markup { Line1 }
            {
                \accidentalStyle modern-cautionary
                r8
                c'4.
                d'2 ~
                d'8
                ef'4
                f'4.
                g'4 ~
                g'4.
                af'8 [
                r8 ]
                bf'4.
                c''2.
                cs''4 ~
                cs''4.
                ef''8 [
                r2 ]
            }
        }
        \context Staff = "Line2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line2 }
            \set Staff.shortInstrumentName = \markup { Line2 }
            {
                \accidentalStyle modern-cautionary
                r2 [
                c'8
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8
                bf'8
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8
                r2 ]
                af''8 [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8
                r2 ]
            }
        }
        \context Staff = "Line3" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Line3 }
            \set Staff.shortInstrumentName = \markup { Line3 }
            {
                \accidentalStyle modern-cautionary
                r2 [
                c'8
                c'8 ]
                ef'4
                ef'4
                g'8 [
                g'8
                bf'8
                bf'8 ]
                cs''4
                cs''4
                f''8 [
                f''8
                r2 ]
                af''8 [
                af''8 ]
                b''4
                b''4
                ef'''4
                ef'''4
                fs'''8 [
                fs'''8
                r2 ]
            }
        }
    >>
}