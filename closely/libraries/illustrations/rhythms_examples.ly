% 2018-02-19 21:55

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context RhythmicStaff = "SIMPLE_BROKEN_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c'8 [ ^ \markup { "SIMPLE_BROKEN_RHYTHM_PATTERN (8)" }
                c'8 ]
                c'4
                c'4
                r4
                r4
                c'4
                c'4
                c'8 [
                c'8 ]
                c'8 [
                c'8 ]
                c'4
                c'4
                r4
                r4
                c'4
                c'4
                c'8 [
                c'8 ]
            }
        }
        \context RhythmicStaff = "UPBEAT_BOOK_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                r8 [
                c'8 ^ \markup { "UPBEAT_BOOK_RHYTHM_PATTERN (8)" }
                r8
                c'8 ]
                c'4
                c'4
                c'4
                c'4
                r8 [
                c'8
                r8
                c'8 ]
                r8 [
                c'8
                r8
                c'8 ]
                c'4
                c'4
                c'4
                c'4
                r8 [
                c'8
                r8
                c'8 ]
            }
        }
    >>
}