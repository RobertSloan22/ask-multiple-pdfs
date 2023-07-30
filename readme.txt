ReadME 
PDF chat verison 1.0
Robert Sloan
www.github.com/RobertSloan22


Ask Multiple PDFs
This is a Streamlit app that allows users to upload multiple PDF documents and ask questions about their content. The app will read through the PDFs, extract the text, and store it in a vector database for quick retrieval.

Features
Upload multiple PDFs
Extract text from PDFs
Break text into chunks
Store text chunks in a vector database
Build a conversational AI agent to answer questions
Chat interface to ask questions and see answers
How it works
The app uses several NLP and AI techniques:

PyPDF2 to extract text from PDFs
langchain to break text into chunks
OpenAI Embeddings to convert text to vectors
FAISS vector store for quick nearest neighbor search
ChatGPT as the conversational agent
Streamlit for the web interface
The vector store allows the chatbot to quickly find relevant passages from the PDFs to answer questions.

Running the app
Clone the repo
Install requirements
Configure Streamlit and .env file
Run streamlit run app.py
Upload PDFs
Ask questions!