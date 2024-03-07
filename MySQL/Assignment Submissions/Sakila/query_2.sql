USE sakila;

SELECT film.film_id, film.title, film.description, film.release_year AS "Relese Year", film.rating, film.special_features, category.name AS "genere" 
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id