USE sakila;

SELECT actor.actor_id, concat_ws(' ',actor.first_name,actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year
FROM actor
JOIN film_actor
ON film_actor.actor_id = actor.actor_id
JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5