from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FAOSTAT Analysis") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

csv_path = "/home/jovyan/dataset/FAOSTAT_data_en_5-20-2025-TEST.csv"

df = spark.read.csv(csv_path, header=True, inferSchema=True)

df.printSchema()
df.show(5)
