from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pinecone
import openai
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

pc = pinecone.Pinecone(api_key=pinecone_api_key)

# Define the index name and specifications
index_name = 'technical-test'
cloud = os.getenv('PINECONE_CLOUD', 'aws')
region = os.getenv('PINECONE_REGION', 'us-east-1')

spec = pinecone.ServerlessSpec(cloud=cloud, region=region)

# Create the index if it does not exist
if index_name not in pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Assuming the dimension of your embeddings is 1536
        metric="cosine",
        spec=spec
    )
    # Wait for the index to be ready
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

index = pc.Index(index_name)

# Initialize OpenAI
openai.api_key = openai_api_key

class Item(BaseModel):
    id: str
    content: str

class Query(BaseModel):
    query: str

@app.post("/insert/")
def insert_item(item: Item):
    embedding = openai.Embedding.create(input=item.content)["data"][0]["embedding"]
    index.upsert(vectors=[{"id": item.id, "values": embedding}])
    return {"message": "Item inserted"}

@app.post("/update/")
def update_item(item: Item):
    embedding = openai.Embedding.create(input=item.content)["data"][0]["embedding"]
    index.upsert(vectors=[{"id": item.id, "values": embedding}])
    return {"message": "Item updated"}

@app.post("/delete/")
def delete_item(item_id: str):
    index.delete(ids=[item_id])
    return {"message": "Item deleted"}

@app.post("/retrieve/")
def retrieve_items(query: Query):
    embedding = openai.Embedding.create(input=query.query)["data"][0]["embedding"]
    results = index.query(vector=embedding, top_k=5, include_values=True)
    return results["matches"]

@app.on_event("shutdown")
def shutdown_event():
    pc.delete_index(index_name)
