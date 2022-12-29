"""
A simple example demonstrating basic Spark SQL features using fictional
data inspired by a paper on determining the optimum length of chopsticks.
https://www.ncbi.nlm.nih.gov/pubmed/15676839
Run with:
  ./bin/spark-submit OptimumChopstick.py
"""
from __future__ import print_function
from pyspark.sql import SparkSession
from pyspark.sql.types import *


def readInput(spark):
	sc = spark.sparkContext
	# Read input by line
	lines = sc.textFile("s3://aws-ps-emr-sme-resources/datasets/chopstick-efficiency/")
	parts = lines.map(lambda l: l.split(","))
	# Each line is converted to a tuple.
	chopstickItems = parts.map(lambda p: (str(p[0]), float(p[1]), int(p[2]), int(p[3].strip())))
	# Define a schema
	fields = [StructField("TestID", StringType()),
		  StructField("FoodPinchingEffeciency", DoubleType()), 
		  StructField("Individual", IntegerType()), 
		  StructField("ChopstickLength", IntegerType())]
	schema = StructType(fields)
	# Apply the schema to the RDD.
	chopsticksDF = spark.createDataFrame(chopstickItems, schema)
	return chopsticksDF


def AvgEffeciencyByLength(df):
	meansDf = df.groupby('ChopstickLength').mean('FoodPinchingEffeciency').orderBy('avg(FoodPinchingEffeciency)',ascending=0)
	return meansDf


if __name__ == "__main__":
	spark = SparkSession.builder.appName("Optimum Chopstick").getOrCreate()
	chopsticksDF = readInput(spark)
	effeciencyByLength = AvgEffeciencyByLength(chopsticksDF)
	effeciencyByLength.show()
	spark.stop()
