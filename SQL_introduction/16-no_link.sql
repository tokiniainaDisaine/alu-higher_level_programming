-- comment
SELECT (
    score,
    name
)
FROM second_table
WHERE name IS NOT EMPTY
ORDER BY DESC