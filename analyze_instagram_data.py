from pyspark.sql import SparkSession
import sys

file_path = sys.argv[1]

spark = SparkSession.builder.appName('InstagramAnalysis').getOrCreate()

# Example: analyze metadata
df = spark.read.text(file_path)

# Do simple word count
word_counts = df.selectExpr("explode(split(value, ' ')) as word").groupBy("word").count()

word_counts.show()

spark.stop()
