from pyspark.sql.functions import col, sum

df.groupBy("Year").agg(
    sum("Value").alias("Total Production")
).orderBy("Year").show()
