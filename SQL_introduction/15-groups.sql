-- comment
SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;