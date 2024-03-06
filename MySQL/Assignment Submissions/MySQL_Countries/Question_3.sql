USE world;

SELECT cities.name, cities.population
FROM cities
JOIN countries
ON cities.country_id = countries.id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC