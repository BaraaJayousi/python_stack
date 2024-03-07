USE sakila;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film_actor.film_id = film.film_id
WHERE film_actor.actor_id = 15 AND film.rating = "G" AND film.special_features like "%behind the scenes%"