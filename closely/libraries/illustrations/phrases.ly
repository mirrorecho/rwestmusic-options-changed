% 2017-09-18 20:40

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "star_line_0" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_line_0 }
            \set Staff.shortInstrumentName = \markup { Star_line_0 }
            {
                bf'4
                c''4
                bf'8 [
                d''8 ]
                g''4
                f''4
                f''4
                ef''4
                d''8 [
                af''8 ]
                af''8 [
                bf''8
                b''8
                fs''8 ]
                bf'4
                bf'4
            }
        }
        \context Staff = "star_line_1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_line_1 }
            \set Staff.shortInstrumentName = \markup { Star_line_1 }
            {
                a'4
                a'4
                a'8 [
                bf'8 ]
                bf'4
                c''4
                d''4
                f'4
                bf'8 [
                bf'8 ]
                bf'8 [
                bf'8
                bf'8
                bf'8 ]
                c''4
                bf'4
            }
        }
        \context Staff = "star_line_2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_line_2 }
            \set Staff.shortInstrumentName = \markup { Star_line_2 }
            {
                e'4
                f'4
                d'8 [
                f'8 ]
                f'4
                bf4
                a'4
                bf4
                g8 [
                ef'8 ]
                cs'8 [
                cs'8
                fs'8
                bf8 ]
                f'4
                f'4
            }
        }
        \context Staff = "star_ii_aconstant_pitch_-2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_ii_aconstant_pitch_-2 }
            \set Staff.shortInstrumentName = \markup { Star_ii_aconstant_pitch_-2 }
            {
                d4
                bf,4
                g8 [
                bf8 ]
                c'4
                bf4
                bf4
                bf,4
                bf,8 [
                cs8 ]
                fs8 [
                f8
                cs8
                ef8 ]
                bf4
                ef'4
            }
        }
    >>
}