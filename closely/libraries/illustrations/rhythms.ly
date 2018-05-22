% 2018-02-19 11:08

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context RhythmicStaff = "STRAIGHT_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "SIMPLE_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "SIMPLE_BROKEN_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "SLOW_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "FLUTTER_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "BUILD_RHYTHM_PATTERNUPBEAT_SPACED_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "CLOCK_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "UPBEAT_CLOCK_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
        \context RhythmicStaff = "FAST_RHYTHM_PATTERN" \with {
            \consists Horizontal_bracket_engraver
        } {
            \clef "percussion"
            {
                c1
                c1
            }
        }
    >>
}