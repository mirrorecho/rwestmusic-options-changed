\version "2.19.82"
\language "english"

\include "../../stylesheets/score.ily"

\header {
    tagline = ##f
}

\layout {}

\paper {}

\score {
    \new Score
    <<
        \context Staff = "Violin1"
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                \accidentalStyle modern-cautionary
                bf8
                [
                a8
                ]
                ef'4
                d'8
                [
                cs'8
                ]
                fs'8
                [
                f'8
                ]
                b'4
                bf'8
                [
                bf'8
                ]
                ef''8
                [
                cs''8
                ]
                af''4
                fs''8
                [
                fs''8
                ]
            }
        }
        \context Staff = "Violin2"
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
        }
        \context Staff = "Viola"
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
        }
        \context Staff = "Cello"
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
        }
    >>
}