USE world;

SELECT countries.name, languages.language, languages.percentage
FROM  countries
JOIN languages
ON countries.id	= languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC