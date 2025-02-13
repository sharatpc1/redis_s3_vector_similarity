import json
import redis
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

# Redis Configuration
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Transformer model configuration
model_name = "bert-base-uncased"  # Change to your preferred transformer model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def embed_text(text):
    """Generate text embeddings using a transformer model."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy().flatten().tolist()

def process_and_store_embeddings(json_file, column_name, redis_key):
    """Read JSON, extract a column, embed it, and store embeddings in Redis."""
    with open(json_file, "r") as file:
        data = json.load(file)

    # Extract the specified column
    column_data = [row[column_name] for row in data if column_name in row]

    # Embed and store each entry in Redis
    for idx, text in enumerate(column_data):
        embedding = embed_text(text)
        redis_client.set(f"{redis_key}:{idx}", json.dumps(embedding))  # Store as JSON string

    print(f"Stored embeddings for '{column_name}' in Redis.")

if __name__ == "__main__":
    json_file_path = "data.json"  # Assume this file exists
    column_name = "text_column"   # Change to the actual column name
    redis_key_prefix = "embeddings"

    process_and_store_embeddings(json_file_path, column_name, redis_key_prefix)
