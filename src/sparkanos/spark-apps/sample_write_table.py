from delta.tables import DeltaTable 
from pyspark.sql import SparkSession 
from pyspark.sql.functions import col 
 
def main(): 
    source_bucket = "bronze" 
 
    spark = SparkSession.builder \ 
        .appName("Write Sample Delta Table to S3") \ 
        .getOrCreate() 
 
    delta_path = f"s3a://{source_bucket}/sample_table" 
 
    data = [ 
        (1, "John Doe", 30), 
        (2, "Jane Smith", 25), 
        (3, "Mike Johnson", 35) 
    ] 
    columns = ["id", "name", "age"] 
 
    df = spark.createDataFrame(data, columns) 
 
    df.show() 
 
    df.write.format("delta").mode("overwrite").save(delta_path) 
 
if __name__ == "__main__": 
    main() 