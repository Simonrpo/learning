# Guidelines for the final project of databases

## 1. Content

1. Stored procedure for creating two related tables.
2. Stored procedure for inserting records into both tables (Minimum 10 records per table).
3. User-defined function that combines at least two database engine functions.
4. Data selection queries from the previously created and populated tables.
  - Minimum three queries.
  - Should include clauses such as:
    - Order By.
    - Group By.
    - Aggregation (sum, avg, min, max, count).
    - Where.
    - Having.
    - Window functions (row_number, rank, dense_rank, sum, avg, min, max, count).
    - Use the previously created user-defined function.
    - Subqueries / Joins / Temporary tables.
  - Each query should be embedded in a view.
5. The project must be presented in a GIT repository with a structure that separates the different types of requested objects."

## 2. Project Presentation:

1. You can work on the exercise in pairs, but the presentation and final grade will be individual.
2. Individual presentation to the professor only.
3. Presentation in English (Attempt 1).
4. Presentation in Spanish (Attempt 2).
5. Two dates for the presentation:
  - March 18 - Group 1
  - March 20 - Group 2

#### Now, let's randomly select the day on which you will present the final project defense using what we have learned

```
WITH EstudiantesNumerados AS (
    SELECT 
        NombreEstudiante,
        ROW_NUMBER() OVER (ORDER BY SUBSTRING(NombreEstudiante, 3, 1)) AS NumeroDeFila
    FROM (
        SELECT 'yurany.bedoyac@comunidad.iush.edu.co' AS NombreEstudiante UNION
        SELECT 'german.bermudezr@comunidad.iush.edu.co' UNION
        SELECT 'dario.borjag@comunidad.iush.edu.co' UNION
        SELECT 'valentina.garciaj@comunidad.iush.edu.co' UNION
        SELECT 'leidy.henaol@comunidad.iush.edu.co' UNION
        SELECT 'fabian.hernandezsa@comunidad.iush.edu.co' UNION
        SELECT 'juan.jaramillov@comunidad.iush.edu.co' UNION
        SELECT 'octavio.moralesg@comunidad.iush.edu.co' UNION
        SELECT 'simon.rodriguezr@comunidad.iush.edu.co' UNION
        SELECT 'diego.salazarc@comunidad.iush.edu.co' UNION
        SELECT 'walther.saldarriagag@comunidad.iush.edu.co' UNION
        SELECT 'diego.santosp@comunidad.iush.edu.co' UNION
        SELECT 'david.tabaress@comunidad.iush.edu.co' UNION
        SELECT 'daniel.villag@comunidad.iush.edu.co'
    ) AS Estudiantes
)

SELECT
    NombreEstudiante,
    CASE WHEN NumeroDeFila % 2 = 0 THEN 'March 13' ELSE 'March 15' END AS DiaExamen
FROM
    EstudiantesNumerados;
```
