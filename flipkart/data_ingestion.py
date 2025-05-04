from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

import os
from flipkart.data_converter import dataconverter
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("STRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE =os.getenv("ASTRA_DB_KEYSPAC")
HF_TOKEN = os.getenv("HF_TOKEN")

embeddings = HuggingFaceInferenceAPIEmbeddings(api_key= HF_TOKEN, model_name= "sentence-transformers/all-MiniLM-L6-v2")

def data_ingestion(ststus):
    vstore= AstraDBVectorStore(
    embedding= embeddings,
    collection_name= "flipkart_chatbot",
    api_endpoint = ASTRA_DB_API_ENDPOINT,
    token = ASTRA_DB_APPLICATION_TOKEN,
    namespace = ASTRA_DB_KEYSPACE

   )
    
    storage = ststus

    if storage == None:
        docs = dataconverter()
        insert_ids = vstore.add_documents(docs)
    else:
        return vstore

    return vstore, insert_ids

#similarity search query

if __name__=="__main__":
    vstore, insert_ids = data_ingestion(None)
    print(f"\n Inserted {len(insert_ids)} documents.")
    result=vstore.similarity_search("can you tell me the low budget sound basshead?")
    for res in result:
       print(f"{{res.page_content}} [{res.metadata}]")

    