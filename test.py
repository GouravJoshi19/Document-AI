import streamlit as st
from pinecone import Pinecone,ServerlessSpec
try:
    cohere_api_key = st.secrets.api_keys.cohere_api_key
    pinecone_api_key = st.secrets.api_keys.pinecone_api_key
    pinecone_index_name = st.secrets.api_keys.pinecone_index
    pinecone_api_env = st.secrets.api_keys.pinecone_api_env
except Exception as e:
    st.write(e)
def create_index(pinecone_api_key,index_name):
    pc=Pinecone(pinecone_api_key=pinecone_api_key)
    index_list=pc.list_indexes().names()
    if index_name not in index_list:
        pc.create_index(
            dimension=1024,
            metric='cosine',
            name=index_name,
            spec=ServerlessSpec(
                region=pinecone_api_env,
                cloud='aws'
            )
        )
    else:
        print("Index already exists")
def main():
    create_index(pinecone_api_key,pinecone_index_name)
    st.success("code ran successfully")
if __name__=="__main__":
    main()