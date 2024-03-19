-- make a best band fans
SELECT ORIGIN AS Origin
SUM(FAN) AS nb_Fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_Fans DESC;
