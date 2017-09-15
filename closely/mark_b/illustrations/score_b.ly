% 2017-09-15 00:05

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
                c'8 [
                f'8 ]
                ef'4
                d'4
                g'8 [
                d'8 ]
                g'8 [
                f'8 ]
                ef'4
                af'4
                ef'8 [
                af'8 ]
                g'8 [
                f'8 ]
                bf'4
                f'4
                bf'8 [
                af'8 ]
            }
        }
        \context Staff = "Clarinet" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { "Clarinet in Bb" }
            \set Staff.shortInstrumentName = \markup { Cl. }
            {
                \accidentalStyle modern-cautionary
                c'8 [
                f'8 ]
                ef'4
                d'4
                g'8 [
                d'8 ]
                g'8 [
                f'8 ]
                ef'4
                af'4
                ef'8 [
                af'8 ]
                g'8 [
                f'8 ]
                bf'4
                f'4
                bf'8 [
                af'8 ]
            }
        }
        \context Staff = "Violin" \with {
            \consists Horizontal_bracket_engraver
        } {
            \set Staff.instrumentName = \markup { Violin }
            \set Staff.shortInstrumentName = \markup { Vln. }
            {
                \accidentalStyle modern-cautionary
                c'8 [
                f'8 ]
                ef'4
                d'4
                g'8 [
                d'8 ]
                g'8 [
                f'8 ]
                ef'4
                af'4
                ef'8 [
                af'8 ]
                g'8 [
                f'8 ]
                bf'4
                f'4
                bf'8 [
                af'8 ]
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
                c8 [
                f8 ]
                ef4
                d4
                g8 [
                d8 ]
                g8 [
                f8 ]
                ef4
                af4
                ef8 [
                af8 ]
                g8 [
                f8 ]
                bf4
                f4
                bf8 [
                af8 ]
            }
        }
    >>
}