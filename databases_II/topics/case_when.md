# CASE WHEN Clause in SQL:

The CASE WHEN clause in SQL is a conditional expression that allows you to perform conditional logic within a query. It is particularly useful for creating customized columns or aggregating data based on specific conditions.

## Usage with Aggregate Functions:

You can use the CASE WHEN clause with aggregate functions to apply conditional logic to the result of an aggregation. This allows you to perform different aggregations based on specific conditions.

### Example 1: Using CASE WHEN with COUNT:

Let's say you have a table named Orders with a column Quantity and you want to count the number of orders falling into different quantity ranges.

```
SELECT
  CASE
    WHEN Quantity >= 1 AND Quantity <= 5 THEN 'Low'
    WHEN Quantity >= 6 AND Quantity <= 10 THEN 'Medium'
    ELSE 'High'
  END AS QuantityRange,
  COUNT(*) AS OrderCount
FROM Orders
GROUP BY QuantityRange;
```


In this example, the CASE WHEN statement categorizes orders into different quantity ranges (Low, Medium, High) based on the Quantity column, and then the COUNT(*) function counts the number of orders in each range.

### Example 2: Using CASE WHEN with AVG:

Suppose you have a table named Employees with a column Salary, and you want to calculate the average salary for different job titles, considering a bonus for managers.

```
SELECT
  JobTitle,
  AVG(
    CASE
      WHEN JobTitle = 'Manager' THEN Salary * 1.1  -- 10% bonus for managers
      ELSE Salary
    END
  ) AS AverageSalary
FROM Employees
GROUP BY JobTitle;
```

In this example, the CASE WHEN statement applies a 10% bonus to the salary for employees with the job title 'Manager' before calculating the average salary using the AVG() function.

These examples demonstrate how the CASE WHEN clause can be employed in SQL for conditional logic within queries and in conjunction with aggregate functions.

### Exercises:

https://www.w3schools.com/sql/sql_case.asp
