import boto3
import pyarrow.parquet as pq
import redis
import io

# AWS S3 Configuration
s3_client = boto3.client('s3', aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key', region_name='your-region')

# Redis Configuration
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def fetch_parquet_from_s3(bucket_name, parquet_file_key):
    # Fetch the Parquet file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=parquet_file_key)
    file_stream = response['Body'].read()

    # Convert file stream to a PyArrow table
    parquet_file = io.BytesIO(file_stream)
    table = pq.read_table(parquet_file)

    return table

def store_parquet_to_redis(table, redis_key_prefix):
    # Extract column names from the Parquet table
    columns = table.schema.names
    redis_client.set(f"{redis_key_prefix}:columns", ",".join(columns))  # Store columns in Redis as a single string
    print(f"Stored columns in Redis: {columns}")
    
    # Store each row from the Parquet table into Redis
    for idx, row in enumerate(table.to_pandas().itertuples(index=False)):
        row_dict = row._asdict()  # Convert each row to a dictionary
        redis_key = f"{redis_key_prefix}:{idx}"
        
        # Storing each row in Redis as a hash
        redis_client.hmset(redis_key, row_dict)
        print(f"Stored row {idx} in Redis with key {redis_key}")

if __name__ == "__main__":
    # Replace with your S3 bucket name and Parquet file key
    bucket_name = 'your-bucket-name'
    parquet_file_key = 'path/to/your/file.parquet'

    # Fetch the Parquet file from S3
    parquet_table = fetch_parquet_from_s3(bucket_name, parquet_file_key)
    
    # Store the Parquet data and columns in Redis
    store_parquet_to_redis(parquet_table, "parquet_data")
