# Cláusula HAVING in SQL:

The **HAVING** clause in SQL is used to filter the results of a query that involves grouping using the GROUP BY clause. While the WHERE clause is used to filter rows before the grouping operation, the HAVING clause is used to filter groups after the grouping operation.

### Example Query:

Let's assume we have a table called Orders containing information about product orders, and we want to find the total sales per customer, but only for customers whose total sales exceed 1000.

```
SELECT CustomerID, SUM(Amount) AS TotalSales
FROM Orders
GROUP BY CustomerID
HAVING SUM(Amount) > 1000;
In this example:
```

The GROUP BY CustomerID clause groups the records by customer identifier.
The SUM(Amount) AS TotalSales clause calculates the total sales for each customer group.
The HAVING SUM(Amount) > 1000 clause filters the results, showing only those groups whose total sales exceed 1000.
This query returns customers whose total sales surpass 1000, providing a filter after the grouping operation.


### Exercises:

https://www.w3schools.com/sql/sql_having.asp
