from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests
import pandas as pd
import numpy as np

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()['embeddings']

    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    # result = r.json()['response']
    result = r.json()
    print(result)

    return result

# Read embeddings df
df = joblib.load('embeddings.joblib')

# Input question and its embedding
incoming_query = input("Ask a question: ")
query_embedding = create_embedding([incoming_query])[0]

# Find similarities between question embeddings and other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [query_embedding]).flatten()
# print(similarities)
top_results = 7
max_indices = similarities.argsort()[::-1][:top_results]
# print(max_indices)

new_df = df.loc[max_indices]
# print(new_df[['title', 'num', 'text']])
# print(new_df.columns)

prompt = f'''I am teaching web development in my Sigma Web Development course. Here are the video subtitle chunks containing the video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[['title', 'num', 'start', 'end', 'text']].to_json(orient = "records")}

--------------

"{incoming_query}"
User asked this question related to the video chunks, you have to answer this in a human way(don't mention the above format, its just for you) how much content is taught in which video(and at what timestamp). Guide the user to go to that particular video. If user asks an unrelated question, tell him you can only answer questions related to the course.
'''

with open('prompt.txt', 'w') as file:
    file.write(prompt)

response = inference(prompt)['response']

with open("response.txt", "w") as file:
    file.write(response)

print("Response printed!")