# Temporary tables in SQL 

Temporary tables in SQL are used to store and manipulate temporary data within the context of a specific session, query, or procedure. They are particularly useful when you need to store intermediate results or work with subsets of data that are relevant for a specific task. Temporary tables exist for a short duration and are automatically dropped when they go out of scope or when the session/connection ends.

## Here are some common scenarios where temporary tables are beneficial:

- **Intermediate Results:** If your query involves complex computations or multiple steps, you might use a temporary table to store intermediate results. This can improve the readability of your query and make it easier to debug.
- **Data Transformation:** Temporary tables are often employed when you need to transform or reshape data before using it in subsequent steps. You can populate a temporary table with the desired format and then work with it.
- **Multi-Step Processing:** In situations where you need to perform several operations on a dataset, using temporary tables allows you to break down the process into manageable steps. Each step can use the results of the previous one.
- **Complex Joins or Aggregations:** When dealing with complex joins or aggregations, temporary tables can help simplify the logic and make the overall query more efficient.

### Common Table Expression (CTE):

*Syntax:* Defined using the WITH clause.

*Scope:* The CTE is valid only for the query in which it is defined.

*Duration:* Exists during the execution of the query.

```
WITH CTEExample AS (
    SELECT * FROM YourTable
)
SELECT * FROM CTEExample;
```

### Local Temporary Tables (#):

*Syntax:* Created using a single hash sign (#) followed by the table name.

*Scope:* The local temporary table is valid only for the user connection that creates it.

*Duration:* Exists until the user connection is closed or explicitly dropped.

```
CREATE TABLE #TempTable (ID INT, Name VARCHAR(50));
```

```
-- Crear una tabla temporal local con # a partir de un SELECT

SELECT *
INTO #TempTableLocal
FROM YourSourceTable
WHERE YourCondition;
```

### Global Temporary Tables (##):

*Syntax:* Created using two hash signs (##) followed by the table name.

*Scope:* The global temporary table is valid for all user connections.

*Duration:* Exists until all connections using it are closed or explicitly dropped.

```
CREATE TABLE ##GlobalTempTable (ID INT, Name VARCHAR(50));
```

```
-- Crear una tabla temporal global con ## a partir de un SELECT

SELECT *
INTO ##TempTableGlobal
FROM YourSourceTable
WHERE YourCondition;
```

### Table Variables (@):

*Syntax:* Defined as table variables using the DECLARE statement with the table's data type.

*Scope:* The table variable is valid only for the code block or stored procedure where it is declared.

*Duration:* Exists until the code block or stored procedure is completed.

```
DECLARE @TempTable TABLE (ID INT, Name VARCHAR(50));
```

```
-- Declarar una variable de tabla con @ y llenarla con un SELECT
DECLARE @TempTableVariable TABLE
(
    Column1 INT,
    Column2 VARCHAR(50)
);

INSERT INTO @TempTableVariable
SELECT Column1, Column2
FROM YourSourceTable
WHERE YourCondition;
```


## Use Cases:

**CTE:** Useful when you need a temporary expression to be referenced in the main query, especially in complex queries.

**Local (#) and Global (##)** Temporary Tables: Useful when you need to store temporary data that must persist across multiple queries within a connection or between connections.

**Table Variables (@):** Useful when you need to store temporary data within a code block or stored procedure but don't require persistence beyond that context.

*The choice of the type of temporary table depends on the scope and duration you need for the temporary data in your specific scenario.*
