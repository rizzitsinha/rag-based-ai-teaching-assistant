# RAG-Based AI Teaching Assistant

This project is a **Retrieval-Augmented Generation (RAG)** based **AI teaching assistant**, built using data from *Code with Harry’s Sigma Web Development Course*. It combines **speech-to-text**, **translation**, **semantic search**, and **LLM-powered Q&A** to provide intelligent responses to user queries about web development concepts.


## 🚀 Features

- **Multimedia Data Processing**  
  Converts educational videos into structured, text-based knowledge for retrieval and reasoning.

- **Automatic Transcription & Translation**  
  Uses **Whisper Large-v2** for high-quality transcription and Hindi → English translation.

- **Semantic Search with Embeddings**  
  Retrieves the most relevant chunks of course content using **bge-m3 embeddings** and **cosine similarity**.

- **LLM-Powered Responses**  
  Employs **Ollama’s Llama3.2** model for generating context-aware answers to user questions.

- **Scalable RAG Pipeline**  
  Clean modular architecture separating preprocessing, embedding generation, and query processing.


## 🛠️ Tech Stack  
- **Python**  
- **Scikit-learn**  
- **Pandas & NumPy**  
- **Matplotlib & Seaborn** (for visualization)  
- **Joblib** (for model saving/loading)  
- **FFmpeg** (for video-to-audio conversion)  
- **Whisper Large-v2** (for transcription and translation)  
- **Ollama (bge-m3 and Llama3.2)** (for embeddings and language model)


## ⚙️ Data Preprocessing Steps

1. **Convert Videos → Audio**  
   Videos from *Code with Harry’s Sigma Web Development Course* were first converted from `.mp4` to `.mp3` using FFmpeg through a Python script.

2. **Transcribe & Translate**  
   Each audio file was processed with **Whisper Large-v2**, which transcribed the Hindi audio and translated it into English.  
   The output was stored as structured JSON files containing the start time, end time, chunk ID, and text of each chunk.

3. **Generate Embeddings**  
   Each chunk’s text was encoded into embeddings using **Ollama’s bge-m3** model. These embeddings capture the semantic meaning of the chunks.

4. **Store Preprocessed Data**  
   The text chunks and their corresponding embeddings were organized into a dictionary and saved in a pickle file using **Joblib** for efficient retrieval.


## 🔍 RAG Pipeline (Query → Answer)

1. **User Query**  
   The user inputs a question related to the web development course.

2. **Query Embedding**  
   The system generates an embedding for the query using **bge-m3**.

3. **Similarity Search**  
   Using **cosine similarity**, the system identifies the top 5 most relevant text chunks from the stored embeddings.

4. **Context Construction**  
   The selected chunks are combined with the original user query to create a context-rich prompt.

5. **LLM Generation**  
   The prompt is passed to **Llama3.2**, which produces an informed and context-aware answer.

## 💡 How to use this RAG-Based AI Teaching Assistant on your own data

1. **Collect your videos**
   Move all your videos into the videos folder

2. **Convert to mp3**
   Convert all the videos into mp3 by running videos_to_mp3.py

3. **Convert mp3 to json**
   Convert all the mp3 files to json by runnig mp3_to_json.py

4. **Convert the json files to Vectors**
   Use the file preprocess_json.py to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

5. **Convert the json files to Vectors**
   Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it into the LLM

## Author

Rishit Sinha  
Github: [rizzitsinha](https://github.com/rizzitsinha)