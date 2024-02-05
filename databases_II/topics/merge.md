# MERGE (UPSERT) in SQL:

The MERGE statement allows you to perform multiple operations in a single statement, typically used for scenarios where you want to insert a record if it doesn't exist or update it if it does.

### Syntax:

```
MERGE INTO target_table USING source_table
ON condition
WHEN MATCHED THEN
  UPDATE SET column1 = value1, column2 = value2, ...
WHEN NOT MATCHED THEN
  INSERT (column1, column2, ...)
  VALUES (value1, value2, ...);
```

### Explanation:

*target_table:* The table you want to modify.

*source_table:* The table providing the data.

*condition:* The condition for matching rows between the target and source tables.

### Example: UPSERTing Employee Information:

Let's assume you have a table EmployeeInfo with columns EmployeeID, Name, and Salary. You want to update the salary if the employee exists or insert a new record if the employee is not present.

```
MERGE INTO EmployeeInfo AS target
USING (VALUES (101, 'John Doe', 50000)) AS source (EmployeeID, Name, Salary)
ON target.EmployeeID = source.EmployeeID
WHEN MATCHED THEN
  UPDATE SET target.Salary = source.Salary
WHEN NOT MATCHED THEN
  INSERT (EmployeeID, Name, Salary)
  VALUES (source.EmployeeID, source.Name, source.Salary);
```


In this example, the MERGE statement checks if there's an existing record for EmployeeID = 101. If yes, it updates the salary; if not, it inserts a new record.

The MERGE statement is a powerful tool for handling upsert scenarios efficiently, providing a concise way to manage changes in a table based on a specified condition.
