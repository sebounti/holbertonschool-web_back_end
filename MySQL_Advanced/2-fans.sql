-- make a best band fans
SELECT origin, SUM(fans) AS nb_Fans FROM metal_bands GROUP BY origin ORDER BY nb_Fans DESC;
