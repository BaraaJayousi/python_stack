USE world;

SELECT name, government_form, capital, life_expectancy
FROM countries 
WHERE government_form = "Constitutional Monarchy" AND life_expectancy > 75 AND capital > 200