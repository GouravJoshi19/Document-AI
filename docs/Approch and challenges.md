# Approach and Decisions

## Frameworks and Software Selection

For this project, I decided to use the following frameworks and tools primarily because of their beginner-friendly nature and my prior experience working with some of them in past projects. Here’s a breakdown of the tools I used and my reasoning behind each:

### Streamlit
- **Reason for Selection**: Streamlit was chosen for the frontend due to its simplicity in building web applications. Its interactive features (like file uploads, chat input, and dynamic responses) are straightforward to implement.
- **Prior Experience**: I had previously used Streamlit for small projects, so it was a natural choice for the UI.

### Langchain
- **Reason for Selection**: This framework was selected for managing AI model chains and conversational workflows. Langchain abstracts complex AI model integrations, making it more accessible to work with.
- **Prior Experience**: I had some prior exposure to Langchain, which made it easier for me to manage the conversational flow in the project.

### Cohere API
- **Reason for Selection**: I opted for Cohere for language model processing, mainly because of its easy-to-use API and sufficient free tier.
- **Prior Experience**: I had previously explored Cohere for text-related tasks, so I was familiar with how to integrate it and retrieve responses.

### Pinecone
- **Reason for Selection**: Using Pinecone was a new experience for me. I had never worked with vector databases or similarity searches before. Learning how to create, query, and store embeddings in Pinecone was a challenge, but I found the documentation and community resources helpful in overcoming this.
- **Learning Experience**: I spent time familiarizing myself with concepts like vector embedding, similarity search, and Pinecone’s indexing mechanisms, which gave me a deeper understanding of how to handle large-scale search problems. Despite the initial learning curve, Pinecone’s scalability and beginner-friendly setup made it a good fit for this project.

### Docker
- **Reason for Selection**: Although I had little experience with Docker, I decided to use it to containerize the application for easier deployment.
- **Learning Experience**: Docker allowed me to ensure consistency across different environments, and it was a great learning experience to understand how to use containers in real-world applications. While challenging, it has been a valuable addition to my skill set.



# Challenges Faced

## 1. API Token Limits
- **Issue**: The free-tier limits of Cohere and Pinecone APIs restricted how many documents and queries could be processed.
- **Solution**: Implemented a method to split large documents into smaller, manageable chunks, allowing them to fit within the API limits.

## 2. Handling Large Documents
- **Issue**: Processing large documents without exceeding API token limits was a challenge.
- **Solution**: By dividing documents into smaller chunks and optimizing API calls, the application was able to handle larger files.

## 3. Learning Docker
- **Issue**: Learning Docker was a steep learning curve for containerizing the project and managing the environment.
- **Solution**: By going through Docker’s official documentation and several tutorials, I was able to understand how to create Dockerfiles and manage containers. Once the basics were clear, Docker made deployment much easier and more consistent across different environments.

## 4. Integration of Multiple Technologies
- **Issue**: Combining multiple technologies (Streamlit, Cohere, Langchain, Pinecone) and making them work smoothly together required significant research and testing.
- **Solution**: Spent extra time understanding the APIs, reading documentation, and testing different setups to ensure everything integrated well. Eventually, by using modular functions, the system became flexible and easier to manage.

## 5. Transitioning to Modular Code
- **Issue**: As a student, I was more used to writing linear code, where all logic is written in one place without much separation of concerns. Transitioning to modular code for this project was a significant challenge, as it required planning and organizing functions in a way that could be reused and scaled, making it more ready for industry-level standards.
- **Solution**: I started by breaking down the main tasks of the application into smaller components or functions, such as document preprocessing, chunking, embedding, and querying. While this took more time upfront, it resulted in cleaner, reusable code. It also helped me see how modularity can benefit future enhancements or debugging processes in a real-world, industry-ready application.
