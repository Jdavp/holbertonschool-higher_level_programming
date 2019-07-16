--  lists all records with a score >= 10 in the table second_table
SELECT score, count(score) AS number FROM second_table GROUP BY score  ORDER BY score DESC;
