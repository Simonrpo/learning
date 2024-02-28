# Database II Workshop 

## DML over Sakila Database (Sample DB for MySQL).

The development of this workshop will assess the ability to execute Data Manipulation Language (DML) statements on the Sakila database running on MySQL.

The development and presentation of this workshop will be done individually, and the date for the presentation will be communicated shortly.


1. Insert a record into the 'film' table using dummy values, ensuring referential integrity with other tables.
2. Which films are longer than the average duration of films?
3. Which films are currently rented at the store with store_id = 1?
4. Of the movies at the store with store_id = 1, which ones were rented for a longer duration than the average rental period?
5. Which actors are part of the cast of 5 or fewer movies?
6. Which last names do not repeat among different actors?
7. Create a view with the top 3 genres that generate the highest revenue. List them in descending order, considering the 'amount' field from the payment table for the calculation.
8. Select the top two most-viewed movies in each city.
9. Select the first name, last name, and email of all customers from the United States who have not made any film rentals in the last three months.
10. Select the top 3 customers from each store based on the number of rentals made. Utilize the Rank, Dense_Rank, and Row_Number functions, and create an additional boolean field indicating records where these three functions return the same value (0) and records where these three functions do not return the same value (1).


### Evaluation:

- 60% -> *Workshop Development.*
- 40% -> *Presentation."*


### Presentation:

Markdown file (.md) with the following structure:

- Stated Exercise.
- Development of the exercise using the ``` tag.
- Image with the statement and its result."

*Example:*

*1. Insert a record into the 'film' table using dummy values, ensuring referential integrity with other tables.*

```
Insert into...
values...
```

![Sakila example](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTxHh5wLkd7ufEkghjtQLQuV7bdZh-E86ZBuGp7kYB5g&s)
