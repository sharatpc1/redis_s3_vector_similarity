# redis_s3_vector_similarity
In this project, I am setting up Redis Stack Server (v6.2.6) on an Amazon EC2 instance. I parse an object from Amazon S3 using Python and the boto3 library. The object is processed and converted into a JSON format . Redis Stack’s vector search capabilities (RedisSearch or RedisAI) allow efficient similarity-based retrieval

Features:
Redis Stack Server Installation: Set up Redis Stack 6.2.6 on an Amazon EC2 instance.
S3 Object Parsing: Fetch and process objects from an S3 bucket.
JSON Storage in Redis: Store structured data as JSON in Redis.
Vector Embeddings: Generate vector representations of text descriptions for semantic search.
Efficient Retrieval: Use Redis Stack’s vector search capabilities to find similar descriptions.

Prerequisites
AWS Account with an EC2 instance running Amazon Linux 2 or Ubuntu.
AWS CLI configured with access to an S3 bucket.
Python 3 with boto3, redis-py, and an embedding model (sentence-transformers or OpenAI API).
url for redis installation file http://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisstack/redisstack-6.2.6-release-notes/
Installation & Setup
1. Install Redis Stack Server 6.2.6 in linux 2 amzon ec2
   wget https://packages.redis.io/redis-stack/redis-stack-server-6.2.6-v13.rhel7.x86_64.tar.gz
   rename the file to redis-6.2.6.tar.gz
   tar xzf redis-6.2.6.tar.gz
   cd redis-stack-server 6.2.6 v13 
   cd bin
   ./redis-stack-server
[image](https://github.com/user-attachments/assets/39c8e073-2c5d-4549-99c5-1461367efd91)

3. check whether the redis is running or not using command
   redis-cli ping
   reply pong
   
5. install redis insight in pc and connect to the redis server hosted in ec2
6.  run the s3_to_redis.py file using python in local pc or in vs-code
7.  run the embedder.py file
8.  you can index the columns and run the queries.
   
