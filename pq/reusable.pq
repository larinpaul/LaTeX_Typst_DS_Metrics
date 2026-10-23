// Reusable Custom Functions

// This file accepts a number named "RatingScore" and returns text
(RatingScore as number) =>
let
    ReviewText = if RatingScore >= 4.5 then "Excellent"
                 else if RatingScore >= 3.5 then "Good"
                 else "Average"
in
    ReviewText
