########################################################################################################################################################

# Nombre de la base de datos en Databricks
database_name = "default"
# Nombre de la tabla que deseas leer
table_name = "netflix"

# Leer la tabla en un DataFrame de Spark
df = spark.table(f"{database_name}.{table_name}")

# Mostrar las primeras filas de la tabla
display(df)

########################################################################################################################################################

from pyspark.sql.functions import col, mean, stddev, min, max, countDistinct, approxCountDistinct
from pyspark.sql.types import IntegerType, LongType, DoubleType

# Mostrar información general del DataFrame
print("Información general del DataFrame:")
print(f"Número total de filas: {df.count()}")
print("Número de columnas:", len(df.columns))

# Obtener información particular de cada columna
print("\nInformación de cada columna:")
for col_name in df.columns:
    print(f"\nColumna: {col_name}")
    print(f"Tipo de datos: {df.schema[col_name].dataType}")
    print(f"Número de valores no nulos: {df.filter(col(col_name).isNotNull()).count()}")
    print(f"Número de valores nulos: {df.filter(col(col_name).isNull()).count()}")
    
    # Si la columna es numérica, calcular estadísticas descriptivas
    if isinstance(df.schema[col_name].dataType, (IntegerType, LongType, DoubleType)):
        stats = df.select(mean(col_name).alias('Mean'),
                          stddev(col_name).alias('Stddev'),
                          min(col_name).alias('Min'),
                          max(col_name).alias('Max')).collect()[0]
        print(f"Media: {stats['Mean']}, Desviación estándar: {stats['Stddev']}")
        print(f"Mínimo: {stats['Min']}, Máximo: {stats['Max']}")
        
        # Histograma (opcional)
        # df.select(col_name).rdd.flatMap(lambda x: x).histogram(10)
        
    # Si la columna es categórica, mostrar valores únicos y frecuencia
    elif df.schema[col_name].dataType in ['StringType']:
        unique_values = df.groupBy(col_name).count().orderBy('count', ascending=False).collect()
        print("Valores únicos:")
        for val in unique_values:
            print(f"{val[col_name]}: {val['count']}")
        
    # Mostrar algunos ejemplos de valores (opcional)
    example_values = df.select(col_name).sample(False, 0.1).limit(5).collect()
    print("Ejemplos de valores:")
    for row in example_values:
        print(row[col_name])

########################################################################################################################################################

from pyspark.sql.functions import split, col

# Dividir la cadena en una lista de valores, utilizando la función split y utilizando la "," como separador
# Posteriormente, nos quedamos con el primer valor [0] de la lista generada
# Este valor lo agregamos a la Columna "MainGenre"
df = df.withColumn("MainGenre", split(col("Genre"), ",")[0])

display(df)

########################################################################################################################################################

from pyspark.sql.functions import regexp_replace, when

# Limpiar la columna "duration" eliminando caracteres no numéricos y convirtiendo valores nulos a 0
# Usaremos la expresión regular [^0-9] para indicar que todo lo que no sean números, sea reemplazado por ""
# La función when nos permite expresar que siempre que el valor sea = "", se lleve un 0, y en cualquier otro caso, se deje el mismo valor de la columna
# Finalmente usamos la función cast para convertir a Integer el DateType de la columna duration 
df = df.withColumn("duration", regexp_replace("duration", "[^0-9]", ""))
df = df.withColumn("duration", when(df["duration"].isNull() , 0).otherwise(df["duration"]).cast("int"))

display(df)

########################################################################################################################################################

# En celdas de código anteriores, hemos importado funciones como when y por ende no hace falta importarlas nuevamente
df = df.filter(df["rating"].isNotNull())

display(df)

########################################################################################################################################################

df.write.mode("overwrite").saveAsTable("default.netflix_refined")

########################################################################################################################################################

%sql

Select
*
from default.netflix_refined

########################################################################################################################################################

%sql

SELECT
t1.MainGenre,
round(avg(t1.rating),2) as Promedio
FROM default.netflix_refined t1
GROUP BY t1.MainGenre
order by 2 DESC

########################################################################################################################################################

import matplotlib.pyplot as plt
import pandas as pd

# Ejecutar la consulta SQL y almacenar los resultados en un DataFrame de Pandas
query_result = spark.sql("""
    SELECT
        t1.MainGenre,
        ROUND(AVG(t1.rating), 2) AS Promedio
    FROM
        default.netflix_refined t1
    WHERE
        t1.MainGenre IS NOT NULL
    GROUP BY
        t1.MainGenre
    ORDER BY
        Promedio DESC
""").toPandas()

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(query_result['MainGenre'], query_result['Promedio'], color='skyblue')
plt.title('Promedio del rating por género')
plt.xlabel('Género')
plt.ylabel('Promedio del rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

########################################################################################################################################################

# Crear un gráfico de puntos
plt.figure(figsize=(10, 6))
plt.plot(query_result['MainGenre'], query_result['Promedio'], marker='o', linestyle='', markersize=8, color='skyblue')
plt.title('Promedio del rating por género')
plt.xlabel('Género')
plt.ylabel('Promedio del rating')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

########################################################################################################################################################
