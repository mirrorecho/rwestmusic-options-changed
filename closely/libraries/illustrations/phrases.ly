% 2018-02-17 13:32

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "StarPhrase_0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { StarPhrase_0 }
            \set Staff.shortInstrumentName = \markup { StarPhrase_0 }
            {
                c'8 [
                d'8 ]
                f'4
                g'4
                ef'4
                af'4
                bf'4
                cs''4
                ef''4
                c''4
                f''8 [
                fs''8
                bf''8
                b''8 ]
                af''4
                cs'''4
                ef'''4
                fs'''4
                af'''4
                e'''4
                a'''8 [
                b'''8
                r2 ]
            }
        }
        \context Staff = "StarPhrase_1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { StarPhrase_1 }
            \set Staff.shortInstrumentName = \markup { StarPhrase_1 }
            {
                f'8 [
                f'8 ]
                bf'4
                bf'4
                af'4
                cs''4
                cs''4
                fs''4
                fs''4
                f''4
                bf''8 [
                bf''8
                ef'''8
                ef'''8 ]
                cs'''4
                fs'''4
                fs'''4
                b'''4
                b'''4
                a'''4
                d''''8 [
                d''''8
                r2 ]
            }
        }
        \context Staff = "StarPhrase_2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { StarPhrase_2 }
            \set Staff.shortInstrumentName = \markup { StarPhrase_2 }
            {
                bf'8 [
                a'8 ]
                ef''4
                d''4
                cs''4
                fs''4
                f''4
                b''4
                bf''4
                bf''4
                ef'''8 [
                cs'''8
                af'''8
                fs'''8 ]
                fs'''4
                b'''4
                bf'''4
                e''''4
                ef''''4
                d''''4
                g''''8 [
                fs''''8
                r2 ]
            }
        }
        \context Staff = "Noneconstant_pitch_-2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Noneconstant_pitch_-2 }
            \set Staff.shortInstrumentName = \markup { Noneconstant_pitch_-2 }
            {
                bf8 [
                bf8 ]
                bf4
                bf4
                bf4
                bf4
                bf4
                bf4
                bf4
                bf4
                bf8 [
                bf8
                bf8
                bf8 ]
                bf4
                bf4
                bf4
                bf4
                bf4
                bf4
                bf8 [
                bf8
                r2 ]
            }
        }
    >>
}