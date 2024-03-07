USE sakila;

SELECT film.film_id, film.title, actor.actor_id, concat_ws(" ",actor.first_name, actor.last_name) AS "Actor Name" , actor.last_update
FROM actor
JOIN film_actor
ON film_actor.actor_id = actor.actor_id
JOIN film
ON film.film_id = film_actor.film_id
WHERE film.film_id = 369