% 2017-09-23 14:27

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "PhraseFlute" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { PhraseFlute }
            \set Staff.shortInstrumentName = \markup { PhraseFlute }
            {
                r8
                a''4.
                g''2 ~
                g''8
                a''4
                b''4.
                a''4 ~
                a''4.
                b''8 [
                r8 ]
                c'''4.
                b''2.
                c'''4 ~
                c'''4.
                d'''8 [
                r2 ]
            }
        }
        \context Staff = "PhraseClarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { PhraseClarinet }
            \set Staff.shortInstrumentName = \markup { PhraseClarinet }
            {
                r8
                g'4.
                a'2 ~
                a'8
                b'4
                a'4.
                b'4 ~
                b'4.
                c''8 [
                r8 ]
                b'4.
                c''2.
                d''4 ~
                d''4.
                c''8 [
                r2 ]
            }
        }
        \context Staff = "PhraseViolin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { PhraseViolin }
            \set Staff.shortInstrumentName = \markup { PhraseViolin }
            {
                r2 [
                b'8
                b'8 ]
                a'4
                a'4
                b'8 [
                b'8
                d''8
                d''8 ]
                c''4
                c''4
                d''8 [
                d''8
                r2 ]
                f''8 [
                f''8 ]
                e''4
                e''4
                f''4
                f''4
                a''8 [
                a''8
                r2 ]
            }
        }
        \context Staff = "PhraseCello" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { PhraseCello }
            \set Staff.shortInstrumentName = \markup { PhraseCello }
            {
                r2 [
                fs8
                fs8 ]
                a4
                a4
                g8 [
                g8
                a8
                a8 ]
                c'4
                c'4
                b8 [
                b8
                r2 ]
                c'8 [
                c'8 ]
                e'4
                e'4
                d'4
                d'4
                e'8 [
                e'8
                r2 ]
            }
        }
    >>
}