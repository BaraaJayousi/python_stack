USE sakila;

SELECT store.store_id, 	address.city_id, customer.first_name, customer.last_name, customer.email, address.address as address
FROM  customer
JOIN address
ON address.address_id = customer.address_id
JOIN store
ON store.store_id = customer.store_id
WHERE store.store_id = 1 AND address.city_id IN (1,42,312,459)