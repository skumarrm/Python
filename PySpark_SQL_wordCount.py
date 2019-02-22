from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from os import path

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.sql.shuffle.partitions", "50") \
    .getOrCreate()


input=spark.read.text("C:\\Users\\smallisudarsan@paypal.com\\Documents\\input.txt")
input.printSchema