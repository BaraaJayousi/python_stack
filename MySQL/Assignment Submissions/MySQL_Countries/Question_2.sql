USE world;

SELECT countries.name, COUNT(cities.id) as Cities
FROM countries
JOIN cities
ON countries.id = cities.country_id
GROUP BY cities.country_id
ORDER BY COUNT(cities.id) DESC