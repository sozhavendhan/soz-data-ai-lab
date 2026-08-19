"""
Simple PySpark word count example (local mode)

Requirements: pyspark
Run:
python foundations/pyspark/example_pyspark_job.py
"""
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[*]").appName("wordcount").getOrCreate()
    data = ["hello world", "hello soz", "spark and pyspark"]
    rdd = spark.sparkContext.parallelize(data)
    counts = rdd.flatMap(lambda x: x.split()) \
               .map(lambda w: (w, 1)) \
               .reduceByKey(lambda a, b: a + b)
    print(sorted(counts.collect()))
    spark.stop()
