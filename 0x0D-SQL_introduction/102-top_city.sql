-- displays top 3 cities during july and august
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
