# Guidelines for the final project of data minning.

## 1. Basic requeriments:

- Select a dataset with at least 8 columns from Kaggle or GitHub.
- Perform an initial profiling at the dataset level.
- Conduct an initial profiling at the column level.
- Based on the profiling and data understanding, document at least four data quality issues and explain why you identified them.
- Subsequently, apply the necessary corrections to address the aforementioned issues.
- From this point forward, make an effort to analyze the data using:
  - SQL queries.
  - Charts.
  - Partial tables.
  - Text created by yourself that describes the behavior of the data.


## 2. Tools:

- You can use the following tools, and the choice will depend on your preference:
  - Databricks Community Edition.
  - Google Colab.
  - Power BI Desktop.
  - Tableau Public.
  - Jupyter Notebooks.
  - RStudio.
  - Excel (Advanced with pivot tables and dynamic charts)
 
*Recuerda que si usas versiones free o comunnity, debes respaldar bien tu trabajo para evitar pérdidas del mismo.*


## 3. Project Presentation:

- You can work on the exercise in pairs, but the presentation and final grade will be individual.
- Individual presentation to the teacher only.
- Presentation in English (Attempt 1).
- Presentation in Spanish (Attempt 2).
- Two dates for the presentation:
  - March 13 - Group 1
  - March 15 - Group 2
 
Now, let's randomly select the day on which you will present the final project defense using what we have learned:

```
WITH EstudiantesNumerados AS (
    SELECT 
        NombreEstudiante,
        ROW_NUMBER() OVER (ORDER BY SUBSTRING(NombreEstudiante, 3, 1)) AS NumeroDeFila
    FROM (
        SELECT 'wilmar.agudeloy@comunidad.iush.edu.co' AS NombreEstudiante UNION
        SELECT 'juan.bustamantes@comunidad.iush.edu.co' UNION
        SELECT 'johan.davidb@comunidad.iush.edu.co' UNION
        SELECT 'juan.delaossa@comunidad.iush.edu.co' UNION
        SELECT 'ana.escobarb@comunidad.iush.edu.co' UNION
        SELECT 'juan.garciame@comunidad.iush.edu.co' UNION
        SELECT 'juan.gaviriagi@comunidad.iush.edu.co' UNION
        SELECT 'jose.gomezj@comunidad.iush.edu.co' UNION
        SELECT 'johan.gonzalezg@comunidad.iush.edu.co' UNION
        SELECT 'isabela.lopezc@comunidad.iush.edu.co' UNION
        SELECT 'pablo.marine@comunidad.iush.edu.co' UNION
        SELECT 'diego.salazarc@comunidad.iush.edu.co' UNION
        SELECT 'maria.valencia@comunidad.iush.edu.co' UNION
        SELECT 'simon.velezg@comunidad.iush.edu.co' UNION
        SELECT 'simon.zapataf@comunidad.iush.edu.co' UNION
        SELECT 'danilo.zapatam@comunidad.iush.edu.co' UNION
        SELECT 'sebastian.zapataz@comunidad.iush.edu.co'
    ) AS Estudiantes
)

SELECT
    NombreEstudiante,
    CASE WHEN NumeroDeFila % 2 = 0 THEN 'March 13' ELSE 'March 15' END AS DiaExamen
FROM
    EstudiantesNumerados;
```
