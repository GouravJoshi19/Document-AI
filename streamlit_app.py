import os
import shutil
import streamlit as st
from dotenv import load_dotenv
from pinecone import Pinecone,ServerlessSpec
from src.methods import get_conversational_chain, get_text_chunks, get_vector_store, load_file

# Constants
WORK_DIR = "data"

# Load environment variables
load_dotenv()
cohere_api_key = st.secrets["COHERE_API_KEY"]
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
pinecone_index_name = st.secrets["PINECONE_INDEX"]
pinecone_api_env = st.secrets["PINECONE_API_ENV"]
# Ensure the working directory exists
if not os.path.exists(WORK_DIR):
    os.mkdir(WORK_DIR)

def preprocess(file):
    """Preprocess the uploaded file by clearing the WORK_DIR and saving the new file."""
    if os.path.exists(WORK_DIR) and os.listdir(WORK_DIR):
        for filename in os.listdir(WORK_DIR):
            file_path = os.path.join(WORK_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    file_path = os.path.join(WORK_DIR, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.read())

    print(f"File saved to {file_path}")
    return file_path 
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
    """Main function to run the Streamlit application."""
    st.set_page_config(page_icon="📑", layout="wide")

    # Add custom CSS
    st.markdown(
        """
        <style>
        .css-1d391kg {  
            font-family: 'Arial', sans-serif; 
            color: #333;
        }
        .stChatMessage {
            background-color: #f0f0f5;
            border-radius: 10px;
        }
        .stSidebar {
            background-color: #e6e6ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Navigation between pages
    page = st.sidebar.selectbox("Select a page:", ("Chat", "Project Details"))

    if page == "Chat":
        # Chat page
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        if "qa_chain" not in st.session_state:
            st.session_state.qa_chain = None

        st.sidebar.header("Document Management")
        
        # File uploader for documents
        docs = st.sidebar.file_uploader("Upload Your Document", type=['pdf', 'csv', 'txt'])

        create_index(pinecone_api_key,pinecone_index_name)
        # Clear chat button in sidebar
        if st.sidebar.button("Clear Chat"):
            st.session_state.chat_history.clear()  # Clear the chat history
            st.sidebar.success("Chat cleared!")

        if docs is not None:
            with st.spinner("Processing your document..."):
                directory = preprocess(docs)
                raw_text = load_file(docs, directory)
                if raw_text:
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.qa_chain = get_conversational_chain(vector_store)
                    st.sidebar.success("Document processed successfully! You can now ask questions.")
                else:
                    st.sidebar.error("Error loading text from the document. Please check the file format.")

        st.header("🤖 Chat Interface")
        st.markdown("✨ Hello! I'm here to help you with your questions. Please upload a document to get started.")

        # Display chat history
        if st.session_state.chat_history:
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                else:
                    st.chat_message("assistant").write(message["content"])

        user_question = st.chat_input("Ask Your Question")
        if user_question:
            if st.session_state.qa_chain is not None:
                st.session_state.chat_history.append({"role": "user", "content": user_question})
                st.chat_message("user").write(user_question)
                
                with st.spinner("Generating answer..."):
                    response = st.session_state.qa_chain.run(user_question)

                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.chat_message("assistant").write(response)


    elif page == "Project Details":
    # Project details page
        st.markdown('<h1 class="header">📘 Project Details</h1>', unsafe_allow_html=True)
        st.markdown("""
        <div class="markdown-text">
        This application allows users to upload various document types (PDF, CSV, TXT) and ask questions related to the content of those documents. 
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<h2 class="subheader">Features:</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **File Upload**: Upload your documents easily using the sidebar.
        - **Conversational Interface**: Interact with the application using a chat-like interface.
        - **Clear Chat**: Reset the conversation with a single button click.
        """)

        st.markdown('<h2 class="subheader">Technologies Used:</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Streamlit**: For building the interactive web interface.
        - **Pinecone**: For vector storage and similarity search.
        - **Cohere**: For natural language processing and understanding.
        - **Langchain**: For managing and chaining different components of language models together to enable complex workflows.
        """)

        st.markdown('<h2 class="subheader">How It Works:</h2>', unsafe_allow_html=True)
        st.markdown("""
        1. Upload a document.
        2. The document is processed, and its content is transformed into text chunks.
        3. These chunks are stored in a vector database.
        4. You can then ask questions about the content, and the application uses a conversational AI model to provide answers.
        """)

        st.markdown('<h2 class="subheader">Limitations:</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Token Limits**: Both Cohere and Pinecone have token limits which might restrict the amount of text that can be processed in one go.
            - Cohere's free tier allows up to 100,000 tokens per month.
            - Pinecone's free tier limits the number of vectors stored and the query capabilities.
        - **Accuracy**: The model's accuracy depends on the quality and relevance of the uploaded documents.
        - **Performance**: Larger documents may take longer to process, and responses may vary based on the complexity of the question.
        """)

        st.markdown('<h2 class="subheader">Getting Started:</h2>', unsafe_allow_html=True)
        st.markdown("""
        - Make sure you have all the necessary API keys configured in your environment.
        - Run the application, upload a document, and start asking questions!
        """)
            
if __name__ == "__main__":
    main()
