from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

df = (spark.read
            .format("csv")
            .option("header", True)
            .option("inferSchema", True)
            .option("delimiter", "|")
            .load("s3://datalake-geovani-igti-edc-desafio-mod1-tf/raw/")
)

(
    df
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-geovani-igti-edc-desafio-mod1-tf/staging/")
)