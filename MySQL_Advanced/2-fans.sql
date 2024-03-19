-- make a best band fans
SELECT origin, SUM(fans) AS nb_Fans GROUP BY origin ORDER BY nb_Fans DESC;
