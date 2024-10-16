## 1. Overview

The **Document Q&A Application** is an innovative web-based tool designed to enhance user interaction with documents through a conversational interface. This application empowers users to upload documents and pose questions related to their content, providing immediate and relevant responses. 

### Purpose
The primary goal of this project is to streamline the process of extracting information from lengthy documents, making it easier for users to find specific details without needing to read through entire texts. This is particularly useful in various fields such as academia, legal studies, and corporate environments, where documents can be extensive and complex.

### Functionality
Key features of the Document Q&A Application include:
- **Document Uploading**: Users can easily upload various document types, such as PDFs and text files.
- **Interactive Chat Interface**: The application allows users to ask questions and receive real-time responses, creating a conversational experience.
- **Information Retrieval**: Using advanced techniques from Langchain, Cohere, and Pinecone, the application processes user queries, retrieves relevant information from uploaded documents, and generates coherent answers.
- **Modular Design**: The codebase is structured in a modular fashion, facilitating easier updates and maintenance, and promoting best practices in software development.

### Significance
By integrating natural language processing and vector databases, this application represents a step towards making information retrieval more intuitive and accessible. It serves as an educational tool for students and a practical solution for professionals dealing with large volumes of text, thereby enhancing productivity and comprehension.

This project not only showcases my ability to integrate multiple technologies but also reflects my commitment to creating user-friendly applications that address real-world challenges in information processing.



## 2. Directory Structure
```
Document-AI/
│
├── data/                       # Directory for storing uploaded files
├── src/
│   ├── methods.py              # Functions for preprocessing, chunking, etc.
│   └── chains.py               # Functions for setting up Langchain conversations
│
├── app.py                      # Main Streamlit application
├── Dockerfile                  # Docker configuration file
├── .dockerignore               # Files and directories to ignore during Docker image build
├── setup.py                    # Setup script for installing the package
├── requirements.txt            # Python dependencies
├── packages.txt                # Apt-get dependencies for deployment (if required)
└── .env                        #for API key storage
└── README.md                   # Project documentation
└── docs/                       # Directory for documentation files
    ├── project_overview.md     # Overview of the project
    ├── pipeline_documentation.md # Documentation for pipeline and deployment

```

## 3. Application Flow

The flow of the Document Q&A Application is designed to facilitate a seamless user experience, guiding users from document upload to query responses. Below is a detailed breakdown of the steps involved:

### 1. Document Upload
- Users begin by uploading their documents using the file uploader provided by Streamlit.
  
### 2. Index Creation
- Upon successful document upload, a method called `create_index` is invoked.
- This method interacts with the Pinecone vector store to create an index using the API key and index name specified in the `.env` file.
- If an index with the specified name already exists, a message is printed in the terminal indicating that "Index already exists." The flow then proceeds to the next step.

### 3. Directory Management
- A directory named `data` is created if it does not already exist. This directory is used to store uploaded documents.
  
### 4. Document Preprocessing
- The uploaded document is passed through a preprocessing method that checks if the `data` directory is empty:
  - **If the directory is empty**: The uploaded file is stored in the directory.
  - **If the directory is not empty**: All files in the directory are deleted before saving the new file.
  
### 5. File Loading
- After the document is saved, the flow moves to the `load_file` method.
- This method utilizes various built-in loaders from Langchain (such as `TextLoader` and `PDFLoader`) to load the document from the `data` directory.
- Once the document's text is extracted, the text is converted into chunks using the `RecursiveCharacterTextSplitter` with a specified chunk size of 1000 characters.

### 6. Create Vector Store
- The chunks are passed into a method called `get_vector_store`. 
- This method first creates embeddings for the chunks using **CohereEmbeddings**.
- The generated embeddings and the original chunks are then used to create a **PineconeVectorStore**. This vector store facilitates efficient similarity searches.

### 7. Conversational Retrieval Chain
- The **PineconeVectorStore** is utilized as a retriever for the conversational retrieval chain.
- This chain leverages **ConversationBufferMemory** from Langchain to maintain the chat history and context of the conversation.

### 8. Session Management
- Streamlit's session state is employed to implement memory, allowing the application to remember past interactions and provide contextually relevant responses to user queries.

### Summary of the Flow
This flow ensures that users can upload their documents easily, while the application efficiently manages document storage and prepares the text for further processing. The careful organization of methods and checks guarantees a smooth transition from document upload to the preparation of text for querying.

## 4. Deployment

This project can be deployed in different environments. Below are the methods to deploy the application, focusing on using Docker and Streamlit Community Cloud.

### Docker Deployment

The application can be easily deployed using Docker, which ensures consistency across different environments. Here’s how to do it:

#### 1. Build the Docker Image

Ensure Docker is installed and running on your machine. To build the Docker image, navigate to the project directory and run:

```
docker build -t Document-AI .
```
#### 2. Run the Docker Container
After building the image, you can run the container using:
```
docker run -p 8501:8501 --env-file .env Document-AI

```
This command will start the Streamlit application inside a Docker container. You can access the application by navigating to http://localhost:8501 in your web browser.

## Streamlit Community Cloud Deployment

To deploy the application on Streamlit Community Cloud, follow these steps:

1. **Create a GitHub Repository**:  
   Create a new repository on GitHub and push your project files there.

2. **Link to Streamlit Community Cloud**:  
   Sign in to Streamlit Community Cloud and select the GitHub repository you just created.

### Environment Variables

Ensure you configure your environment variables in the Streamlit Cloud settings. You can add your API keys and other necessary environment variables like this:

```
COHERE_API_KEY=<your-cohere-api-key>
PINECONE_API_KEY=<your-pinecone-api-key>
PINECONE_INDEX=<your-pinecone-index-name>
PINECONE_API_ENV=<pinecone-environment-region>
```
3. **Deploy**:
Once you’ve set everything up, click on the “Deploy” button, and Streamlit will handle the deployment process.

## Considerations
Ensure that your API keys are valid and that you have the necessary permissions to access the services (Cohere and Pinecone). 

Monitor the usage of API tokens, especially if you are using free-tier services, to avoid hitting limits during operation.


```
Feel free to modify any specific parts or add additional instructions based on your experience!
```


## 5. Testing and Validation

Testing is an essential part of software development that ensures the application works as expected. In this project, I focused on manual testing due to my limited experience with automated testing frameworks.

### Manual Testing
- **Functionality Testing**: I manually tested key features of the application, such as:
    - Uploading documents and checking if they are processed correctly.
    - Asking questions through the chat interface and verifying that the responses are relevant and accurate.
    - Checking the performance of the application under different conditions (e.g., uploading different sizes of documents).

While I did not implement automated tests, I recognized their importance and plan to explore testing frameworks such as `pytest` and `unittest` in future projects to ensure more robust testing.
