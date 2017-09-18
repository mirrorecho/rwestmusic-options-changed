% 2017-09-17 20:17

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
                r8
                c'4.
                d'2 ~
                d'8
                f'4
                g'4.
                ef'4 ~
                ef'4.
                af'8 [
                r8 ]
                bf'4.
                cs''2.
                ef''4 ~
                ef''4.
                c''8 [
                r2 ]
            }
        }
        \context Staff = "star_line_1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_line_1 }
            \set Staff.shortInstrumentName = \markup { Star_line_1 }
            {
                r8
                f'4.
                f'2 ~
                f'8
                bf'4
                bf'4.
                af'4 ~
                af'4.
                cs''8 [
                r8 ]
                cs''4.
                fs''2.
                fs''4 ~
                fs''4.
                f''8 [
                r2 ]
            }
        }
        \context Staff = "star_line_2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_line_2 }
            \set Staff.shortInstrumentName = \markup { Star_line_2 }
            {
                r8
                bf'4.
                a'2 ~
                a'8
                ef''4
                d''4.
                cs''4 ~
                cs''4.
                fs''8 [
                r8 ]
                f''4.
                b''2.
                bf''4 ~
                bf''4.
                bf''8 [
                r2 ]
            }
        }
        \context Staff = "star_i_aconstant_pitch_-2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Star_i_aconstant_pitch_-2 }
            \set Staff.shortInstrumentName = \markup { Star_i_aconstant_pitch_-2 }
            {
                r8
                bf4.
                bf2 ~
                bf8
                bf4
                bf4.
                bf4 ~
                bf4.
                bf8 [
                r8 ]
                bf4.
                bf2.
                bf4 ~
                bf4.
                bf8 [
                r2 ]
            }
        }
    >>
}