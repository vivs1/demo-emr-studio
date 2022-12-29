
# Import pyspark 
from pyspark.sql import SparkSession
import time

# Create SparkSession
spark = SparkSession.builder \
          .appName('SparkByExamples.com') \
          .getOrCreate()
         
#EMP DataFrame
empData = [(1,"Smith",10,None,3000),
    (2,"Rose",20,"M",4000),
    (3,"Williams",10,"M",1000),
    (4,"Jones",10,"F",2000),
    (5,"Brown",30,"",-1),
    (6,"Brown",30,"",-1)
  ]
  
empColumns = ["emp_id","name","dept_id",
  "gender","salary"]
empDF = spark.createDataFrame(empData,empColumns)
empDF.show()

# Get row count
rows = empDF.count()

# Get columns count
cols = len(empDF.columns)

print(f"DataFrame Dimensions : {(rows,cols)}")
print(f"DataFrame Rows count : {rows}")
print(f"DataFrame Columns count : {cols}")

# distinct count
distinct_count = empDF.distinct().count()

# functions.count()
from pyspark.sql.functions import count
empDF.select(count(empDF.name)).show()
empDF.select(count(empDF.name), count(empDF.gender)).show()

# using agg
empDF.agg({'name':'count','gender':'count'}).show()

# groupby count
empDF.groupBy("dept_id").count().show()

# PySpark SQL Count
empDF.createOrReplaceTempView("EMP")
spark.sql("SELECT COUNT(*) FROM EMP").show()
spark.sql("SELECT COUNT(distinct dept_id) FROM EMP").show()
spark.sql("SELECT DEPT_ID,COUNT(*) FROM EMP GROUP BY DEPT_ID").show()

#counter
count = 0

max_num = 75
for i in range(max_num):
    # if (i%10 ==5):
      print(i)
      time.sleep(1.0000)
