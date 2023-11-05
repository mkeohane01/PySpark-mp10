from pyspark.sql import SparkSession

def log_stuff(stuff, file = "outputs.md"):
  # log stuff to a file
  with open(file, "a") as f:
    f.write(stuff + "\n")

def load_data(spark, csv="data/baseball_data.csv"):
  # load the csv data from the url and return a dataframe
  df = spark.read.csv(csv, header=True)
  return df

def spark_query(spark, df, query="SELECT * FROM baseball_table"):
  # create a temp view of the dataframe
  df.createOrReplaceTempView("baseball_table")
  # query the data and log the result
  result = spark.sql(query)
  return result

def spark_transformation(spark, df):
  # transform the data by grouping by team and position and counting the number of players
  transformed_df = df.groupBy("Team", "PosCategory").count()
  # sort the data by team and position
  transformed_df = transformed_df.orderBy(["Team", "PosCategory"], ascending=[1, 1])
  return transformed_df


def main():
  # clear the outputs file
  with open("outputs.md", "w") as f:
    f.write("")

  # create a spark session
  spark = SparkSession.builder.appName("Baseball").getOrCreate()
  log_stuff("Spark session created.")

  # load the data
  df = load_data(spark)
  log_stuff("Data loaded.")

  # query the data
  query = "SELECT Name FROM baseball_table WHERE Team = 'WAS' and PosCategory = 'Pitcher' LIMIT 10" 
  query_result = spark_query(spark, df, query=query)
  log_stuff(f"Query executed: {query}")
  log_stuff(query_result.toPandas().to_markdown())

  # transform the data
  transformed_df = spark_transformation(spark, df)
  log_stuff("Data transformed: Grouped by team and position and counted the number of players")
  log_stuff(transformed_df.toPandas().to_markdown())

  # stop the spark session
  spark.stop()
  log_stuff("Spark session stopped.")

  


if __name__ == "__main__":
  main()
