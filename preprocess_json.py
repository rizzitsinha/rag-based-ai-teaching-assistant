import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Function to create embedding
def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()['embeddings']

    return embedding

# List and sort all jsons
jsons = os.listdir("jsons")
# Removing hidden files from jsons list
jsons = [file for file in jsons if not file.startswith('.')]
jsons.sort()

# Create a list to store chunks, along with their embeddings
my_dicts = []

for json_file in jsons:

    with open(f"jsons/{json_file}", 'r') as file:
        data = json.load(file)

    print(f"Creating embedding for {json_file}")
    # Create embeddings for all chunks
    embeddings = create_embedding([c['text'] for c in data['chunks']])

    for i, chunk in enumerate(data['chunks']):
        chunk['embedding'] = embeddings[i]
        my_dicts.append(chunk)

    print(f"Embedding created for {json_file}")



df = pd.DataFrame.from_records(my_dicts)
# Save this dataframe
joblib.dump(df, 'embeddings.joblib')

