########################################################################################################################################################

# Nombre de la base de datos en Databricks
database_name = "default"
# Nombre de la tabla que deseas leer
table_name = "google_play_store"

# Leer la tabla en un DataFrame de Spark
df = spark.table(f"{database_name}.{table_name}")

# Mostrar el esquema de la tabla
df.printSchema()

# Mostrar las primeras filas de la tabla
display(df)

########################################################################################################################################################

#Análisis y perfilamiento básico de dataset
from pyspark.sql.functions import col

# Mostrar información general del DataFrame
print("Información general del DataFrame:")
print(f"Número total de filas: {df.count()}")
print("Primeras filas del DataFrame:")
df.show(5)

# Obtener información particular de cada columna
print("Información particular de cada columna:")
for col_name in df.columns:
    print(f"\nColumna: {col_name}")
    print(f"Tipo de datos: {df.schema[col_name].dataType}")
    print(f"Número de valores no nulos: {df.filter(col(col_name).isNotNull()).count()}")
    print(f"Número de valores únicos: {df.select(col_name).distinct().count()}")

    # Si es posible, calcular estadísticas descriptivas
    if df.schema[col_name].dataType in ["IntegerType()", "DoubleType()", "DoubleType", "double"]:
        print("Estadísticas descriptivas:")
        df.describe([col_name]).show()

########################################################################################################################################################

# Creación de nueva columna "Last Updated Date" con formato de fecha
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import DateType

# 1. Crear una nueva columna llamada "Last Updated Date"
# 2. Crear la nueva columna a partir de la columna "Last Updated"
df = df.withColumn("Last Updated Date", to_date(col("Last Updated"), "MMMM d, yyyy"))

# 3. La nueva columna debe quedar en formato Date
# 4. Eliminar la columna "Last Updated"
df = df.drop("Last Updated")

# 5. Imprimir resultado usando display
display(df)


########################################################################################################################################################
