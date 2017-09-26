% 2017-09-23 16:42

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
                {
                    \accidentalStyle modern-cautionary
                    {
                        R1 * 1
                    }
                    r8
                    bf'4. \startGroup
                    c''2 ~
                    c''8
                    ef''4.
                    g''2 ~
                    g''8 [
                    c'''8 \stopGroup
                    r8
                    c'''8 ~ ] \startGroup
                    c'''4
                    cs'''4 ~
                    cs'''4.
                    c'''8 ~
                    c'''4
                    g''4 ~
                    g''4.
                    ef''8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r8
                    bf'4. \startGroup
                    f''2 ~
                    f''8
                    ef''4
                    ef''8 ~
                    ef''8
                    f''4
                    f''8 ~
                    f''8
                    ef''4.
                    ef''2 ~
                    ef''8 [
                    d''8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    c''8 \startGroup
                    d''8
                    ef''8 ]
                    bf''8 [
                    bf''8
                    r8
                    f''8 \stopGroup ]
                    r8 [
                    cs'''8 \startGroup
                    f''8
                    c'''8 ]
                    r8 [
                    g''8 \stopGroup
                    r4 ]
                    r8 [
                    f''8 \startGroup
                    bf'8
                    g''8 ]
                    r8 [
                    c'''8 \stopGroup
                    r8
                    af''8 ] \startGroup
                    bf''8 [
                    fs''8
                    r8
                    d''8 \stopGroup ]
                    r8 [
                    ef''8 \startGroup
                    c''8
                    c''8 ]
                    r8 [
                    bf'8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    c''8 \startGroup
                    f''8
                    g''8 ]
                    r8 [
                    a''8 \stopGroup
                    r8
                    g''8 ] \startGroup
                    r8 [
                    e''8 \stopGroup
                    r8
                    f''8 ] \startGroup
                    r8 [
                    e''8 \stopGroup
                    r4 ]
                    r8 [
                    bf'8 \startGroup
                    d''8
                    f''8 ]
                    r8 [
                    d''8 \stopGroup
                    r8
                    d'''8 ] \startGroup
                    r8 [
                    e'''8 \stopGroup
                    r8
                    f''8 ] \startGroup
                    r8 [
                    e''8 \stopGroup
                    r4 ]
                    r8 [
                    ef''8 \startGroup
                    f''8
                    g''8 ]
                    e''8 [
                    e''8
                    e'''8
                    d'''8 ]
                    bf''8 [
                    e''8
                    c''8
                    e''8 ]
                    e''8 [
                    a'8
                    r8
                    b'8 \stopGroup ]
                    r8 [
                    f'8 \startGroup
                    ef''8
                    d''8 ]
                    c'''8 [
                    bf''8
                    a''8
                    g''8 ]
                    f''8 [
                    e''8
                    d''8
                    c''8 ]
                    b'8 [
                    a'8
                    g''8
                    fs''8 ]
                    e''8 [
                    d'''8
                    r8
                    cs'''8 \stopGroup ]
                    b'2 \startGroup
                    a'4
                    b'4
                    fs''4
                    b''4
                    fs''4
                    b''4
                    d'''4
                    bf''4 \stopGroup
                    b'4 \startGroup
                    a'4
                    b'4
                    fs''4
                    b''4
                    fs''4
                    b''4
                    d'''4
                    bf''2 ~ \stopGroup
                    bf''2
                }
                {
                    \accidentalStyle modern-cautionary
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
                    {
                        R1 * 1
                    }
                    r2
                    b'4 \startGroup
                    cs''4
                    b'8 [
                    ds''8 ]
                    gs''4
                    fs''4 \stopGroup
                    fs''4 \startGroup
                    e''4
                    ds''8 [
                    a''8 ]
                    a''8 [
                    b''8
                    c'''8
                    g''8 ]
                    b'4
                    b'4 \stopGroup
                    r2
                    r2
                    r8
                    e''4. \startGroup
                    fs''2 ~
                    fs''8
                    g''4
                    fs''8 ~
                    fs''4
                    g''4 ~
                    g''4.
                    a''8 \stopGroup
                    r8
                    g''4. \startGroup
                    a''2 ~
                    a''4
                    b''4 ~
                    b''4.
                    a''8 \stopGroup
                    r8
                    a''4. \startGroup
                    g''2 ~
                    g''8
                    a''4
                    b''8 ~
                    b''4
                    a''4 ~
                    a''4.
                    b''8 \stopGroup
                    r8
                    c'''4. \startGroup
                    b''2 ~
                    b''4
                    c'''4 ~
                    c'''4.
                    d'''8 \stopGroup
                    c''4 \startGroup
                    d''4
                    c''8 [
                    e''8 ]
                    a''4
                    g''4 \stopGroup
                    g''4 \startGroup
                    f''4
                    e''8 [
                    bf''8 ]
                    bf''8 [
                    c'''8
                    df'''8
                    af''8 ]
                    c''4
                    c''4 \stopGroup
                    ef''4. \startGroup
                    c''8 ~
                    c''8
                    c''4
                    d''8
                    c''4 \stopGroup
                    ef''4 ~ \startGroup
                    ef''8
                    f''4
                    c'''8 ~
                    c'''8 [
                    af''8 ]
                    ef''4 \stopGroup
                    bf'4. \startGroup
                    g'8 ~
                    g'8
                    g'4
                    a'8
                    g'4 \stopGroup
                    bf'4 ~ \startGroup
                    bf'8
                    c''4
                    g''8 ~
                    g''8 [
                    ef''8 ]
                    bf'4 \stopGroup
                    f''4. \startGroup
                    d''8 ~
                    d''8
                    d''4
                    e''8
                    d''4 \stopGroup
                    f''4 ~ \startGroup
                    f''8
                    g''4
                    d'''8 ~
                    d'''8 [
                    bf''8 ]
                    f''4 \stopGroup
                    {
                        R1 * 2
                    }
                }
            }
        }
        \context Staff = "Clarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                {
                    \accidentalStyle modern-cautionary
                    {
                        R1 * 1
                    }
                    r8
                    f'4. \startGroup
                    a'2 ~
                    a'8
                    af'4.
                    ef'2 ~
                    ef'8 [
                    ef''8 \stopGroup
                    r8
                    f''8 ~ ] \startGroup
                    f''4
                    ef''4 ~
                    ef''4.
                    bf'8 ~
                    bf'4
                    c''4 ~
                    c''4.
                    g'8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r8
                    f'4. \startGroup
                    a'2 ~
                    a'8
                    bf'4
                    g'8 ~
                    g'8
                    bf'4
                    af'8 ~
                    af'8
                    bf'4.
                    g'2 ~
                    g'8 [
                    bf'8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    f'8 \startGroup
                    g'8
                    bf'8 ]
                    cs''8 [
                    bf'8
                    r8
                    ef''8 \stopGroup ]
                    r8 [
                    bf'8 \startGroup
                    ef''8
                    f'8 ]
                    r8 [
                    bf'8 \stopGroup
                    r4 ]
                    r8 [
                    bf8 \startGroup
                    c'8
                    f'8 ]
                    r8 [
                    c''8 \stopGroup
                    r8
                    cs''8 ] \startGroup
                    d''8 [
                    c''8
                    r8
                    bf'8 \stopGroup ]
                    r8 [
                    c''8 \startGroup
                    ef'8
                    bf8 ]
                    r8 [
                    d'8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    bf8 \startGroup
                    c'8
                    f'8 ]
                    r8 [
                    cs''8 \stopGroup
                    r8
                    c''8 ] \startGroup
                    r8 [
                    af'8 \stopGroup
                    r8
                    bf'8 ] \startGroup
                    r8 [
                    af'8 \stopGroup
                    r4 ]
                    r8 [
                    d'8 \startGroup
                    f'8
                    g'8 ]
                    r8 [
                    cs''8 \stopGroup
                    r8
                    c''8 ] \startGroup
                    r8 [
                    af'8 \stopGroup
                    r8
                    bf'8 ] \startGroup
                    r8 [
                    d''8 \stopGroup
                    r4 ]
                    r8 [
                    e'8 \startGroup
                    g'8
                    a'8 ]
                    c''8 [
                    a'8
                    bf'8
                    e''8 ]
                    c''8 [
                    d''8
                    e'8
                    d'8 ]
                    b8 [
                    e'8
                    r8
                    fs'8 \stopGroup ]
                    r8 [
                    ef'8 \startGroup
                    af'8
                    c''8 ]
                    bf'8 [
                    ef''8
                    d''8
                    c''8 ]
                    bf'8 [
                    fs'8
                    g'8
                    bf'8 ]
                    fs'8 [
                    d'8
                    c'8
                    e'8 ]
                    a'8 [
                    c''8
                    r8
                    b'8 \stopGroup ]
                    b2 \startGroup
                    c'4
                    e'4
                    b'4
                    c''4
                    b'4
                    cs''4
                    b'4
                    cs''4 \stopGroup
                    b4 \startGroup
                    c'4
                    e'4
                    b'4
                    c''4
                    b'4
                    cs''4
                    b'4
                    cs''2 ~ \stopGroup
                    cs''2
                }
                {
                    \accidentalStyle modern-cautionary
                    r8
                    b'4. \startGroup
                    ds'2 ~
                    ds'8
                    fs'4
                    b'8 ~
                    b'4
                    b'4 ~
                    b'4.
                    a'8 \stopGroup
                    r8
                    fs'4. \startGroup
                    g'2 ~
                    g'4
                    g'4 ~
                    g'4.
                    fs'8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r2
                    as'4 \startGroup
                    as'4
                    as'8 [
                    b'8 ]
                    b'4
                    cs''4 \stopGroup
                    ds''4 \startGroup
                    fs'4
                    b'8 [
                    b'8 ]
                    b'8 [
                    b'8
                    b'8
                    b'8 ]
                    cs''4
                    b'4 \stopGroup
                    r2
                    r2
                    r8
                    fs'4. \startGroup
                    g'2 ~
                    g'8
                    fs'4
                    g'8 ~
                    g'4
                    a'4 ~
                    a'4.
                    g'8 \stopGroup
                    r8
                    a'4. \startGroup
                    b'2 ~
                    b'4
                    a'4 ~
                    a'4.
                    b'8 \stopGroup
                    r8
                    g'4. \startGroup
                    a'2 ~
                    a'8
                    b'4
                    a'8 ~
                    a'4
                    b'4 ~
                    b'4.
                    c''8 \stopGroup
                    r8
                    b'4. \startGroup
                    c''2 ~
                    c''4
                    d''4 ~
                    d''4.
                    c''8 \stopGroup
                    b'4 \startGroup
                    b'4
                    b'8 [
                    c''8 ]
                    c''4
                    d''4 \stopGroup
                    e''4 \startGroup
                    g'4
                    c''8 [
                    c''8 ]
                    c''8 [
                    c''8
                    c''8
                    c''8 ]
                    d''4
                    c''4 \stopGroup
                    g'4. \startGroup
                    af'8 ~
                    af'8
                    af'4
                    g'8
                    g'4 \stopGroup
                    c''4 ~ \startGroup
                    c''8
                    c''4
                    df''8 ~
                    df''8 [
                    ef''8 ]
                    af'4 \stopGroup
                    d'4. \startGroup
                    ef'8 ~
                    ef'8
                    ef'4
                    d'8
                    d'4 \stopGroup
                    g'4 ~ \startGroup
                    g'8
                    g'4
                    af'8 ~
                    af'8 [
                    bf'8 ]
                    ef'4 \stopGroup
                    a'4. \startGroup
                    bf'8 ~
                    bf'8
                    bf'4
                    a'8
                    a'4 \stopGroup
                    d''4 ~ \startGroup
                    d''8
                    d''4
                    ef''8 ~
                    ef''8 [
                    f''8 ]
                    bf'4 \stopGroup
                    {
                        R1 * 2
                    }
                }
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                {
                    \accidentalStyle modern-cautionary
                    {
                        R1 * 1
                    }
                    r8
                    c''4. \startGroup
                    f''2 ~
                    f''8
                    cs''4.
                    c''2 ~
                    c''8 [
                    bf'8 \stopGroup
                    r8
                    c'8 ~ ] \startGroup
                    c'4
                    af4 ~
                    af4.
                    g'8 ~
                    g'4
                    d'4 ~
                    d'4.
                    c''8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r8
                    c''4. \startGroup
                    bf'2 ~
                    bf'8
                    af'4
                    bf'8 ~
                    bf'8
                    bf4
                    c'8 ~
                    c'8
                    cs'4.
                    bf2 ~
                    bf8 [
                    g'8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    bf''8 \startGroup
                    bf'8
                    af'8 ]
                    ef'8 [
                    f'8
                    r8
                    bf8 \stopGroup ]
                    r8 [
                    af8 \startGroup
                    bf8
                    g'8 ]
                    r8 [
                    f'8 \stopGroup
                    r4 ]
                    r8 [
                    ef''8 \startGroup
                    d''8
                    c''8 ]
                    r8 [
                    af'8 \stopGroup
                    r8
                    c'8 ] \startGroup
                    c'8 [
                    cs'8
                    r8
                    f'8 \stopGroup ]
                    r8 [
                    bf'8 \startGroup
                    g'8
                    c''8 ]
                    r8 [
                    f''8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    f''8 \startGroup
                    d''8
                    c''8 ]
                    r8 [
                    e'8 \stopGroup
                    r8
                    c'8 ] \startGroup
                    r8 [
                    b8 \stopGroup
                    r8
                    c'8 ] \startGroup
                    r8 [
                    b8 \stopGroup
                    r4 ]
                    r8 [
                    f''8 \startGroup
                    d''8
                    c''8 ]
                    r8 [
                    a'8 \stopGroup
                    r8
                    g'8 ] \startGroup
                    r8 [
                    b8 \stopGroup
                    r8
                    d'8 ] \startGroup
                    r8 [
                    b8 \stopGroup
                    r4 ]
                    r8 [
                    af''8 \startGroup
                    e''8
                    e'8 ]
                    g'8 [
                    d'8
                    ef'8
                    a8 ]
                    e'8 [
                    g'8
                    f'8
                    g'8 ]
                    a'8 [
                    g''8
                    r8
                    e''8 \stopGroup ]
                    r8 [
                    bf'8 \startGroup
                    fs'8
                    g'8 ]
                    f'8 [
                    fs'8
                    g'8
                    fs'8 ]
                    ef'8 [
                    d'8
                    c''8
                    f''8 ]
                    a''8 [
                    g''8
                    f''8
                    b'8 ]
                    fs'8 [
                    g'8
                    r8
                    fs'8 \stopGroup ]
                    g''2 \startGroup
                    f''4
                    b'4
                    a'4
                    g'4
                    b4
                    a4
                    b4
                    fs'4 \stopGroup
                    g''4 \startGroup
                    f''4
                    b'4
                    a'4
                    g'4
                    b4
                    a4
                    b4
                    fs'2 ~ \stopGroup
                    fs'2
                }
                {
                    \accidentalStyle modern-cautionary
                    r8
                    cs'4. \startGroup
                    fs'2 ~
                    fs'8
                    e'4
                    gs'8 ~
                    gs'4
                    d'4 ~
                    d'4.
                    d'8 \stopGroup
                    r8
                    d'4. \startGroup
                    d'2 ~
                    d'4
                    b4 ~
                    b4.
                    b8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r2
                    f'4 \startGroup
                    fs'4
                    ds'8 [
                    fs'8 ]
                    fs'4
                    b4 \stopGroup
                    as'4 \startGroup
                    b4
                    gs8 [
                    e'8 ]
                    d'8 [
                    d'8
                    g'8
                    b8 ]
                    fs'4
                    fs'4 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    d'8 \startGroup [
                    d'8 ]
                    e'4
                    e'4
                    g'8 [
                    g'8 \stopGroup ]
                    fs'8 \startGroup [
                    fs'8 ]
                    g'4
                    g'4
                    b'8 [
                    b'8 \stopGroup ]
                    r2
                    a'8 \startGroup [
                    a'8 ]
                    b'4
                    b'4
                    d''4
                    d''4
                    c''8 [
                    c''8 \stopGroup ]
                    r2
                    b'8 \startGroup [
                    b'8 ]
                    a'4
                    a'4
                    b'8 [
                    b'8 \stopGroup ]
                    d''8 \startGroup [
                    d''8 ]
                    c''4
                    c''4
                    d''8 [
                    d''8 \stopGroup ]
                    r2
                    f''8 \startGroup [
                    f''8 ]
                    e''4
                    e''4
                    f''4
                    f''4
                    a''8 [
                    a''8 \stopGroup ]
                    gf'4 \startGroup
                    g'4
                    e'8 [
                    g'8 ]
                    g'4
                    c'4 \stopGroup
                    b'4 \startGroup
                    c'4
                    a8 [
                    f'8 ]
                    ef'8 [
                    ef'8
                    af'8
                    c'8 ]
                    g'4
                    g'4 \stopGroup
                    c'4. \startGroup
                    ef'8 ~
                    ef'8
                    f'4
                    c''8
                    c''4 \stopGroup
                    c''4 ~ \startGroup
                    c''8
                    c''4
                    f'8 ~
                    f'8 [
                    c''8 ]
                    df''4 \stopGroup
                    g4. \startGroup
                    bf8 ~
                    bf8
                    c'4
                    g'8
                    g'4 \stopGroup
                    g'4 ~ \startGroup
                    g'8
                    g'4
                    c'8 ~
                    c'8 [
                    g'8 ]
                    af'4 \stopGroup
                    d'4. \startGroup
                    f'8 ~
                    f'8
                    g'4
                    d''8
                    d''4 \stopGroup
                    d''4 ~ \startGroup
                    d''8
                    d''4
                    g'8 ~
                    g'8 [
                    d''8 ]
                    ef''4 \stopGroup
                    {
                        R1 * 2
                    }
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
                {
                    \accidentalStyle modern-cautionary
                    {
                        R1 * 1
                    }
                    r8
                    c'4. \startGroup
                    d'2 ~
                    d'8
                    c'4.
                    bf2 ~
                    bf8 [
                    f8 \stopGroup
                    r8
                    af,8 ~ ] \startGroup
                    af,4
                    c4 ~
                    c4.
                    ef8 ~
                    ef4
                    c4 ~
                    c4.
                    c'8 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    r8
                    bf4. \startGroup
                    d'2 ~
                    d'8
                    cs'4
                    bf8 ~
                    bf8
                    ef4
                    bf,8 ~
                    bf,8
                    af,4.
                    bf,2 ~
                    bf,8 [
                    c8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    bf8 \startGroup
                    c'8
                    cs'8 ]
                    af8 [
                    ef8
                    r8
                    bf,8 \stopGroup ]
                    r8 [
                    ef8 \startGroup
                    bf,8
                    bf8 ]
                    r8 [
                    c'8 \stopGroup
                    r4 ]
                    r8 [
                    c'8 \startGroup
                    g8
                    c'8 ]
                    r8 [
                    ef8 \stopGroup
                    r8
                    fs8 ] \startGroup
                    g,8 [
                    af,8
                    r8
                    c8 \stopGroup ]
                    r8 [
                    af8 \startGroup
                    c'8
                    f'8 ]
                    r8 [
                    c'8 \stopGroup
                    r4 ]
                    r2
                    r8 [
                    c'8 \startGroup
                    bf8
                    c'8 ]
                    r8 [
                    c8 \stopGroup
                    r8
                    f8 ] \startGroup
                    r8 [
                    c8 \stopGroup
                    r8
                    ef8 ] \startGroup
                    r8 [
                    c8 \stopGroup
                    r4 ]
                    r8 [
                    c'8 \startGroup
                    bf8
                    d'8 ]
                    r8 [
                    e8 \stopGroup
                    r8
                    f8 ] \startGroup
                    r8 [
                    d8 \stopGroup
                    r8
                    ef8 ] \startGroup
                    r8 [
                    af8 \stopGroup
                    r4 ]
                    r8 [
                    bf8 \startGroup
                    c'8
                    d'8 ]
                    f8 [
                    e8
                    f8
                    e8 ]
                    f8 [
                    c'8
                    bf8
                    a8 ]
                    e'8 [
                    d'8
                    r8
                    e'8 \stopGroup ]
                    r8 [
                    fs'8 \startGroup
                    cs'8
                    fs8 ]
                    fs8 [
                    af8
                    fs8
                    f8 ]
                    fs8 [
                    a8
                    fs8
                    fs'8 ]
                    e'8 [
                    fs'8
                    fs'8
                    fs8 ]
                    d8 [
                    fs8
                    r8
                    fs,8 \stopGroup ]
                    d'2 \startGroup
                    b4
                    af4
                    d4
                    e4
                    ef4
                    e4
                    g4
                    b4 \stopGroup
                    d'4 \startGroup
                    b4
                    af4
                    d4
                    e4
                    ef4
                    e4
                    g4
                    b2 ~ \stopGroup
                    b2
                }
                {
                    \accidentalStyle modern-cautionary
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
                    {
                        R1 * 1
                    }
                    r2
                    ds4 \startGroup
                    b,4
                    gs8 [
                    b8 ]
                    cs'4
                    b4 \stopGroup
                    b4 \startGroup
                    b,4
                    b,8 [
                    d8 ]
                    g8 [
                    fs8
                    d8
                    e8 ]
                    b4
                    e'4 \stopGroup
                    r2
                    {
                        R1 * 1
                    }
                    d8 \startGroup [
                    d8 ]
                    cs4
                    cs4
                    d8 [
                    d8 \stopGroup ]
                    fs8 \startGroup [
                    fs8 ]
                    e4
                    e4
                    fs8 [
                    fs8 \stopGroup ]
                    r2
                    a8 \startGroup [
                    a8 ]
                    g4
                    g4
                    a4
                    a4
                    c'8 [
                    c'8 \stopGroup ]
                    r2
                    fs8 \startGroup [
                    fs8 ]
                    a4
                    a4
                    g8 [
                    g8 \stopGroup ]
                    a8 \startGroup [
                    a8 ]
                    c'4
                    c'4
                    b8 [
                    b8 \stopGroup ]
                    r2
                    c'8 \startGroup [
                    c'8 ]
                    e'4
                    e'4
                    d'4
                    d'4
                    e'8 [
                    e'8 \stopGroup ]
                    e4 \startGroup
                    c4
                    a8 [
                    c'8 ]
                    d'4
                    c'4 \stopGroup
                    c'4 \startGroup
                    c4
                    c8 [
                    ef8 ]
                    af8 [
                    g8
                    ef8
                    f8 ]
                    c'4
                    f'4 \stopGroup
                    c4. \startGroup
                    df8 ~
                    df8
                    c4
                    c8
                    f4 \stopGroup
                    af4 ~ \startGroup
                    af8
                    bf4
                    af8 ~
                    af8 [
                    bf8 ]
                    c'4 \stopGroup
                    g,4. \startGroup
                    af,8 ~
                    af,8
                    g,4
                    g,8
                    c4 \stopGroup
                    ef4 ~ \startGroup
                    ef8
                    f4
                    ef8 ~
                    ef8 [
                    f8 ]
                    g4 \stopGroup
                    d4. \startGroup
                    ef8 ~
                    ef8
                    d4
                    d8
                    g4 \stopGroup
                    bf4 ~ \startGroup
                    bf8
                    c'4
                    bf8 ~
                    bf8 [
                    c'8 ]
                    d'4 \stopGroup
                    {
                        R1 * 2
                    }
                }
            }
        }
    >>
    \midi {}
}