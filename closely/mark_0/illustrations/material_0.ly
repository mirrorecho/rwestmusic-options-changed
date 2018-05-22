% 2018-05-08 23:56

\version "2.19.54"
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
                r2.
            }
        }
        \context Staff = "FasterRhythm" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { FasterRhythm }
            \set Staff.shortInstrumentName = \markup { FasterRhythm }
            {
                c'8 [
                c'8
                r2. ]
            }
        }
        \context Staff = "SlowPhrase0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { SlowPhrase0 }
            \set Staff.shortInstrumentName = \markup { SlowPhrase0 }
            {
                e'4
                r2.
            }
        }
        \context Staff = "FastPhrase0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { FastPhrase0 }
            \set Staff.shortInstrumentName = \markup { FastPhrase0 }
            {
                e'8 [
                f'8
                r2. ]
            }
        }
        \context Staff = "Phrase0_I" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Phrase0_I }
            \set Staff.shortInstrumentName = \markup { Phrase0_I }
            {
                r1
                r1
                e'4
                f'2
                a4 ~
                a2
                b2 ~
                b4
                fs2
                g'4
                a'4
                c'2
                d'4
                a4
                bf'2
                c''4
                e'4
                f'2
                c'4
                r1
            }
        }
        \context Staff = "Phrase0_II" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Phrase0_II }
            \set Staff.shortInstrumentName = \markup { Phrase0_II }
            {
                r1
                r1
                r1
                fs8 [
                d8 ]
                f'4
                d4
                f'4
                b4
                f'8 [
                b8
                g'8
                b8 ]
                g'4
                c'4
                g'8 [
                c'8
                a8
                c'8 ]
                a4
                c''4
                a8 [
                c''8
                f'8
                c''8
                f'8
                d''8 ]
                f'8 [
                d''8 ]
                g'4
                d''4
                g'8 [
                e'8 ]
                g'8 [
                e'8
                g''8
                e'8
                g''8
                c''8 ]
                g''4
                c''4
                af''8 [
                c''8
                af''8
                d''8 ]
                af''4
                d''4
                bf'8 [
                d''8
                bf'8
                cs'''8
                bf'8
                cs'''8 ]
            }
        }
    >>
}