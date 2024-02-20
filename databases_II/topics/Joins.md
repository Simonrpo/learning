# Introduction to SQL Joins:

In SQL, a join is a method used to combine rows from two or more tables based on a related column between them. Joins are fundamental in relational databases as they allow you to retrieve data from multiple tables simultaneously.

## Types of SQL Joins:

### 1. Inner Join:

- Retrieves rows from both tables where the join condition is met.
- If there's no match between the tables, those rows are excluded from the result set.

```
SELECT *
FROM table1
INNER JOIN table2 ON table1.column = table2.column;
```

### 2. Left (Outer) Join:

- Returns all rows from the left table (first table) and matching rows from the right table (second table).
- If there's no match in the right table, NULL values are included in the result set.

```
SELECT *
FROM table1
LEFT JOIN table2 ON table1.column = table2.column;
```

### 3. Right (Outer) Join:

- Opposite of Left Join. Returns all rows from the right table and matching rows from the left table.
- If there's no match in the left table, NULL values are included.

```
SELECT *
FROM table1
RIGHT JOIN table2 ON table1.column = table2.column;
```

### 4.Full (Outer) Join:

- Returns all rows when there's a match in either left or right table.
- If there's no match, NULL values are included.

```
SELECT *
FROM table1
FULL JOIN table2 ON table1.column = table2.column;
```

### 5. Cross Join:

- Also known as Cartesian Join. Returns the Cartesian product of the two tables.
- Combines each row of the first table with every row of the second table.

```
SELECT *
FROM table1
CROSS JOIN table2;
```

### *Example:*

Suppose we have two tables, "employees" and "departments". To find the department each employee belongs to, we can use a Left Join:

```
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;
```

This query retrieves all employees, including those without a department, and their corresponding department names if they have one.

## Conclusion:

SQL joins are powerful tools for combining data from multiple tables in a relational database. Understanding the different types of joins and when to use them is essential for querying and analyzing complex datasets efficiently.


![SQL Joins](https://i.stack.imgur.com/FYwNJ.png)
