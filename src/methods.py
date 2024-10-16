import os
from dotenv import load_dotenv
from langchain.llms import Cohere
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import CohereEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import  Docx2txtLoader, CSVLoader, TextLoader,PyPDFLoader


load_dotenv()
cohere_api_key = os.getenv('COHERE_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index_name = os.getenv("PINECONE_INDEX")
pinecone_api_env=os.getenv('PINECONE_API_ENV')

def load_file(docs,directory):
    text = []
    

    # Handle single file upload
    if docs.name.endswith(".pdf"):
        loader=PyPDFLoader(directory)
        text.extend(loader.load())
    
    # Handle .txt files
    if docs.name.endswith(".txt"):
        loader=TextLoader(directory,encoding='UTF-8')
        text.extend(loader.load())

    # Handle .csv files
    elif docs.name.endswith(".csv"): 
        loader = CSVLoader(directory)
        text.extend(loader.load())

    # Handle .docx files
    elif docs.name.endswith(".docx"):
        loader = Docx2txtLoader(directory)
        text += loader.load()

    return text

def get_text_chunks(text):
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
    chunks=splitter.split_documents(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings=CohereEmbeddings(model='embed-english-v3.0',user_agent='langchain')
    vector_store=PineconeVectorStore.from_documents(
            text_chunks,
            pinecone_api_key=pinecone_api_key,
            embedding=embeddings,
            index_name=pinecone_index_name
    )
    return vector_store
def get_conversational_chain(vector_store):
    llm=Cohere(cohere_api_key=cohere_api_key)
    memory=ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    chain=ConversationalRetrievalChain.from_llm(llm=llm,retriever=vector_store.as_retriever(),memory=memory)
    return chain

