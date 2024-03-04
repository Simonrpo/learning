# Triggering Database Actions

## Introduction:

In the realm of database management, the initiation of various actions can be orchestrated through three distinct methods: manual invocation, event-driven triggers, and scheduled events.

### 1. Manual Invocation:

In scenarios where user intervention is pivotal, manual triggering serves as a direct and intentional initiation of actions within the database. This method provides users with control over when specific operations are executed, ensuring a hands-on approach to data management.

### 2. Event-Driven Triggers:

Event-driven triggers respond to predefined events occurring within the database, such as INSERT, UPDATE, or DELETE operations on specific tables. These triggers automatically execute associated actions in response to the unfolding of events, ensuring consistency, enforcing business rules, and automating tasks based on dynamic conditions.

### 3. Scheduled Events:

Scheduled events involve the execution of predefined actions based on a calendared or time-based schedule. This method allows for the automation of recurring tasks, data maintenance, and other operations at specified intervals, ensuring timely and routine execution.

```
CREATE EVENT monthly_maintenance
ON SCHEDULE EVERY 1 MONTH
DO
```

## Types of Event-Driven Triggers:

#### BEFORE Triggers:

Executed before the specified event (e.g., INSERT, UPDATE, DELETE) occurs.
Often used for validation or modifying data before it is written to the database.

```
CREATE TRIGGER before_insert_example
BEFORE INSERT ON your_table
FOR EACH ROW
BEGIN
    -- Trigger logic goes here
END;
```

#### AFTER Triggers:

Executed after the specified event has occurred.
Commonly used for tasks such as logging changes or updating related tables.

```
CREATE TRIGGER after_update_example
AFTER UPDATE ON your_table
FOR EACH ROW
BEGIN
    -- Trigger logic goes here
END;
```


#### INSTEAD OF Triggers:

Instead of executing the original statement, the trigger is executed.
Useful for customizing or replacing the default action of an event.

```
CREATE TRIGGER instead_of_delete_example
INSTEAD OF DELETE ON your_table
BEGIN
    -- Trigger logic goes here
END;
```

## Common Use Cases for Triggers:

#### Enforcing Business Rules:

Use triggers to enforce complex business rules and ensure data consistency.

#### Audit Trail Logging:

Create triggers to log changes made to specific tables for auditing purposes.

#### Automated Data Modifications:

Implement triggers to automatically update related tables when changes occur.

#### Custom Validation:

Utilize triggers for custom validation logic before allowing data modifications.


## Conclusion:

Triggers play a crucial role in database management by providing a mechanism to automate actions based on specific events. Understanding the types of triggers and their applications allows database administrators and developers to enhance data integrity and automate routine tasks within a database system.
