from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import time
import numpy as np
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader



load_dotenv()

OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
EMBEDDINGS_MODEL_DEPLOYMENT_NAME = os.getenv("EMBEDDINGS_MODEL_DEPLOYMENT_NAME")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# Load documents from the 'docs' directory
persona_li = ["manager", "agent", "cxo"]


# Initialize OpenAIEmbeddings
embeddings = OpenAIEmbeddings(
    openai_api_base=OPENAI_API_BASE,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type=OPENAI_API_TYPE,
    openai_api_version=OPENAI_API_VERSION,
    deployment=EMBEDDINGS_MODEL_DEPLOYMENT_NAME
)
# Batch mechanism to create vector databases with a sleep interval
batch_size = 15  # You can adjust the batch size as needed


for x in persona_li:
    path = 'docs/'+ x
    documents = []
    for file in os.listdir(path):
        if file.lower().endswith('.pdf'):
            input_file_path = os.path.join(path, file)
            loader = PyPDFLoader(input_file_path)
            documents.extend(loader.load())
        elif file.endswith('.docx') or file.endswith('.doc'):
            doc_path = './docs/' + file
            loader = Docx2txtLoader(doc_path)
            documents.extend(loader.load())
        elif file.endswith('.csv'):
            print(file)
            input_file_path = os.path.join(path, file)
            loader = CSVLoader(input_file_path)
            documents.extend(loader.load())
        elif file.endswith('.txt') or file.endswith('.md'):
            print(file)
            input_file_path = os.path.join(path, file)
            loader = TextLoader(input_file_path)
            documents.extend(loader.load())
        

    # Split documents using the CharacterTextSplitter
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)

    
    total_chunks = len(chunked_documents)
    print(total_chunks)
    chunks_processed = 0
    faiss_dbs = []

    batch = chunked_documents[chunks_processed: chunks_processed + batch_size]
    final_db = FAISS.from_documents(batch, embeddings)
    chunks_processed += batch_size
    time.sleep(5)

    while chunks_processed < total_chunks:
        # Take a batch of chunks
        batch = chunked_documents[chunks_processed: chunks_processed + batch_size]

        # Create vector database for the current batch
        db_batch = FAISS.from_documents(batch, embeddings)
        final_db.merge_from(db_batch)
    
        # Append the current batch vector database to the list

        # Update the number of processed chunks
        chunks_processed += batch_size
        print(chunks_processed)
        # Add a sleep interval between batches (adjust as needed)
        time.sleep(10)

    # Save the final index to a local file
    final_db.save_local("faiss_index/faiss_index_"+x)