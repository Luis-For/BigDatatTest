from pyspark.sql import SparkSession

# Conectarse al Spark Master del clúster en Docker
spark = SparkSession.builder \
    .appName("VSCode_Spark_Analysis") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# Leer archivo montado en el contenedor Jupyter (si estás accediendo al mismo volumen)
df = spark.read.csv("/home/jovyan/dataset/FAOSTAT_data_en_5-20-2025-TEST.csv", header=True, inferSchema=True)

df.show(5)
