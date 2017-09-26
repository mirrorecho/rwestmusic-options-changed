% 2017-09-23 20:21

\version "2.19.54"
\language "english"

\include "../../stylesheets/score.ily"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Flute" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Flute }
            \set Staff.shortInstrumentName = \markup { Fl. }
            {
                \accidentalStyle modern-cautionary
                r8
                bf'4. \startGroup
                a'2 ~
                a'8
                ef''4
                d''8 ~
                d''4
                df''4 ~
                df''4.
                gf''8 \stopGroup
                r8
                f''4. \startGroup
                b''2 ~
                b''4
                bf''4 ~
                bf''4.
                bf''8 \stopGroup
                r4
                d'4 \startGroup
                c'4
                g'8 [
                f'8 ]
                f'4
                bf'4 \stopGroup
                a'4 \startGroup
                ef''4
                d''8 [
                df''8
                gf''8
                f''8 ]
                b''8 [
                bf''8 ]
                bf''4
                ef'''4 \stopGroup
                r4
                bf'4. \startGroup
                df''8 ~
                df''8
                ef''4
                c''8
                f''4 \stopGroup
                gf''4 ~ \startGroup
                gf''8
                bf''4
                b''8 ~
                b''8 [
                gs''8 ]
                cs'''4 ~ \stopGroup
                cs'''2
                r8
                fs''4. \startGroup
                b''2 ~
                b''8
                b''4
                b''8 ~
                b''4
                a''4 ~
                a''4.
                g''8 \stopGroup
                r8
                b''4. \startGroup
                c'''2 ~
                c'''4
                b''4 ~
                b''4.
                b''8 \stopGroup
                r2
                fs''4 \startGroup
                e''4
                ds''8 [
                a''8
                a''8
                b''8 ]
                c'''8 [
                g''8 ]
                b'4
                b'4 \stopGroup
                r4
                d''4. \startGroup
                b'8 ~
                b'8
                b'4
                cs''8
                b'4 \stopGroup
                d''4 ~ \startGroup
                d''8
                e''4
                b''8 ~
                b''8 [
                g''8 ]
                d''4 ~ \stopGroup
                d''2
                r8
                g''4. \startGroup
                c'''2 ~
                c'''8
                c'''4
                c'''8 ~
                c'''4
                as''4 ~
                as''4.
                gs''8 \stopGroup
                r8
                c'''4. \startGroup
                cs'''2 ~
                cs'''4
                c'''4 ~
                c'''4.
                c'''8 \stopGroup
                r2
                {
                    R1 * 6
                }
            }
        }
        \context Staff = "Clarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                \accidentalStyle modern-cautionary
                r8
                f'4. \startGroup
                f'2 ~
                f'8
                bf'4
                bf'8 ~
                bf'4
                af'4 ~
                af'4.
                df''8 \stopGroup
                r8
                df''4. \startGroup
                gf''2 ~
                gf''4
                gf''4 ~
                gf''4.
                f''8 \stopGroup
                r4
                a4 \startGroup
                a4
                d'8 [
                d'8 ]
                c'4
                f'4 \stopGroup
                f'4 \startGroup
                bf'4
                bf'8 [
                af'8
                df''8
                df''8 ]
                gf''8 [
                gf''8 ]
                f''4
                bf''4 \stopGroup
                r4
                df'4. \startGroup
                gf'8 ~
                gf'8
                gf'4
                f'8
                bf'4 \stopGroup
                bf'4 ~ \startGroup
                bf'8
                ef''4
                ef''8 ~
                ef''8 [
                df''8 ]
                gf''4 ~ \stopGroup
                gf''2
                r8
                b'4. \startGroup
                ds''2 ~
                ds''8
                fs''4
                b''8 ~
                b''4
                b''4 ~
                b''4.
                a''8 \stopGroup
                r8
                fs''4. \startGroup
                g''2 ~
                g''4
                g''4 ~
                g''4.
                fs''8 \stopGroup
                r2
                ds''4 \startGroup
                fs'4
                b'8 [
                b'8
                b'8
                b'8 ]
                b'8 [
                b'8 ]
                cs''4
                b'4 \stopGroup
                r4
                fs'4. \startGroup
                g'8 ~
                g'8
                g'4
                fs'8
                fs'4 \stopGroup
                b'4 ~ \startGroup
                b'8
                b'4
                c''8 ~
                c''8 [
                d''8 ]
                g'4 ~ \stopGroup
                g'2
                r8
                c''4. \startGroup
                e'2 ~
                e'8
                g'4
                c''8 ~
                c''4
                c''4 ~
                c''4.
                as'8 \stopGroup
                r8
                g'4. \startGroup
                gs'2 ~
                gs'4
                gs'4 ~
                gs'4.
                g'8 \stopGroup
                r2
                {
                    R1 * 6
                }
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                \accidentalStyle modern-cautionary
                r4
                c'4
                c'4 \startGroup
                d'8 [
                d'8 ]
                f'8 [
                f'8
                g'8
                g'8 ]
                ef'4
                ef'4
                af'4 \stopGroup
                af'4
                r4
                bf'4
                bf'4 \startGroup
                df''8 [
                df''8 ]
                ef''4
                ef''4
                c''4 \stopGroup
                c''4
                r4
                e4 \startGroup
                f4
                a8 [
                bf8 ]
                g4
                c'4 \stopGroup
                d'4 \startGroup
                f'4
                g'8 [
                ef'8
                af'8
                bf'8 ]
                df''8 [
                ef''8 ]
                c''4
                f''4 \stopGroup
                r4
                bf4. \startGroup
                bf8 ~
                bf8
                bf4
                bf8
                bf4 \stopGroup
                bf4 ~ \startGroup
                bf8
                bf4
                bf8 ~
                bf8 [
                bf8 ]
                bf'4 ~ \stopGroup
                bf'2
                r8
                cs''4. \startGroup
                fs''2 ~
                fs''8
                e''4
                gs''8 ~
                gs''4
                d''4 ~
                d''4.
                d''8 \stopGroup
                r8
                d''4. \startGroup
                d''2 ~
                d''4
                b'4 ~
                b'4.
                b'8 \stopGroup
                r2
                as'4 \startGroup
                b4
                gs8 [
                e'8
                d'8
                d'8 ]
                g'8 [
                b8 ]
                fs'4
                fs'4 \stopGroup
                r4
                b4. \startGroup
                d'8 ~
                d'8
                e'4
                b'8
                b'4 \stopGroup
                b'4 ~ \startGroup
                b'8
                b'4
                e'8 ~
                e'8 [
                b'8 ]
                c''4 ~ \stopGroup
                c''2
                r8
                d'4. \startGroup
                g'2 ~
                g'8
                f'4
                a'8 ~
                a'4
                ds'4 ~
                ds'4.
                ds'8 \stopGroup
                r8
                ds'4. \startGroup
                ds'2 ~
                ds'4
                c'4 ~
                c'4.
                c'8 \stopGroup
                r2
                {
                    R1 * 6
                }
            }
        }
        \context Staff = "Cello" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Vc. }
            \clef "bass"
            {
                \accidentalStyle modern-cautionary
                r4
                bf,4
                bf,4 \startGroup
                bf,8 [
                bf,8 ]
                bf,8 [
                bf,8
                bf,8
                bf,8 ]
                bf,4
                bf,4
                bf,4 \stopGroup
                bf,4
                r4
                bf,4
                bf,4 \startGroup
                bf,8 [
                bf,8 ]
                bf,4
                bf,4
                bf,4 \stopGroup
                bf,4
                r4
                bf,4 \startGroup
                bf,4
                bf,8 [
                bf,8 ]
                bf,4
                bf,4 \stopGroup
                bf,4 \startGroup
                bf,4
                bf,8 [
                bf,8
                bf,8
                bf,8 ]
                bf,8 [
                bf,8 ]
                bf,4
                bf,4 \stopGroup
                r4
                f,4. \startGroup
                b,8 ~
                b,8
                as,4
                as,8
                ds4 \stopGroup
                cs4 ~ \startGroup
                cs8
                gs4
                fs8 ~
                fs8 [
                fs8 ]
                b4 ~ \stopGroup
                b2
                r8
                b4. \startGroup
                as2 ~
                as8
                b4
                ds'8 ~
                ds'4
                e'4 ~
                e'4.
                b8 \stopGroup
                r8
                b4. \startGroup
                b2 ~
                b4
                e'4 ~
                e'4.
                cs'8 \stopGroup
                r2
                b4 \startGroup
                b,4
                b,8 [
                d8
                g8
                fs8 ]
                d8 [
                e8 ]
                b4
                e'4 \stopGroup
                r4
                b,4. \startGroup
                c8 ~
                c8
                b,4
                b,8
                e4 \stopGroup
                g4 ~ \startGroup
                g8
                a4
                g8 ~
                g8 [
                a8 ]
                b4 ~ \stopGroup
                b2
                r8
                c'4. \startGroup
                b2 ~
                b8
                c'4
                e'8 ~
                e'4
                f'4 ~
                f'4.
                c'8 \stopGroup
                r8
                c'4. \startGroup
                c'2 ~
                c'4
                f'4 ~
                f'4.
                d'8 \stopGroup
                r2
                {
                    R1 * 6
                }
            }
        }
    >>
    \midi {}
}