-- lists number of records with the same score in second_table
SELECT score, COUNT(*) AS number GROUP BY score
ORDER BY number DESC;
