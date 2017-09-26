% 2017-09-23 21:30

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
                r8
                g''4. \startGroup
                c'''2 ~
                c'''8
                c'''4
                c'''4.
                bf''4 ~
                bf''4.
                af''8 \stopGroup [
                r8 ]
                c'''4. \startGroup
                df'''2.
                c'''4 ~
                c'''4.
                c'''8 \stopGroup [
                r2 ]
            }
        }
        \context Staff = "StarPhrase_1" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { StarPhrase_1 }
            \set Staff.shortInstrumentName = \markup { StarPhrase_1 }
            {
                r8
                c''4. \startGroup
                e'2 ~
                e'8
                g'4
                c''4.
                c''4 ~
                c''4.
                bf'8 \stopGroup [
                r8 ]
                g'4. \startGroup
                af'2.
                af'4 ~
                af'4.
                g'8 \stopGroup [
                r2 ]
            }
        }
        \context Staff = "StarPhrase_2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { StarPhrase_2 }
            \set Staff.shortInstrumentName = \markup { StarPhrase_2 }
            {
                r8
                d'4. \startGroup
                g'2 ~
                g'8
                f'4
                a'4.
                ef'4 ~
                ef'4.
                ef'8 \stopGroup [
                r8 ]
                ef'4. \startGroup
                ef'2.
                c'4 ~
                c'4.
                c'8 \stopGroup [
                r2 ]
            }
        }
        \context Staff = "f_star_viiconstant_pitch_-2" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { F_star_viiconstant_pitch_-2 }
            \set Staff.shortInstrumentName = \markup { F_star_viiconstant_pitch_-2 }
            {
                r8
                c'4. \startGroup
                b2 ~
                b8
                c'4
                e'4.
                f'4 ~
                f'4.
                c'8 \stopGroup [
                r8 ]
                c'4. \startGroup
                c'2.
                f'4 ~
                f'4.
                d'8 \stopGroup [
                r2 ]
            }
        }
    >>
}