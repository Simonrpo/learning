-----------------------------------------------------------------

SELECT 
customer_id,
email,
replace(left(email, locate("@", email)-1), ".", "") usuario
FROM sakila.customer;

-----------------------------------------------------------------

SELECT 
concat(concat(substring(first_name, 1, 1), lower(substring(first_name, 2, length(first_name)))), 
" ", 
concat(substring(last_name, 1, 1), lower(substring(last_name, 2, length(last_name))))) as Nombre_Completo
FROM sakila.actor;

-----------------------------------------------------------------

SELECT
t_film.title,
t_film_conteo.conteo_rentas
from sakila.film t_film
INNER JOIN sakila.film_category t_film_category
ON t_film.film_id = t_film_category.film_id
INNER JOIN sakila.category t_category
ON t_film_category.category_id = t_category.category_id
INNER JOIN 
(SELECT 
t1.film_id,
count(t1.film_id) as conteo_rentas 
FROM sakila.inventory T1
INNER JOIN sakila.rental T2
ON T1.inventory_id = T2.inventory_id
group by t1.film_id) t_film_conteo
ON t_film_conteo.film_id = t_film.film_id
where t_category.name = "Drama"
order by 2 desc
limit 5;

-----------------------------------------------------------------
