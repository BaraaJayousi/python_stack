USE world;

SELECT countries.region, count(*)
FROM countries
GROUP BY  countries.region
ORDER BY count(*) DESC