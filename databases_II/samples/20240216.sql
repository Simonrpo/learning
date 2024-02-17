-----------------------------------------------------------------

SELECT 
customer_id,
email,
replace(left(email, locate("@", email)-1), ".", "") usuario
FROM sakila.customer;

-----------------------------------------------------------------
