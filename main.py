import logging
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

############################################
# Initiate LLM on Pinecone
############################################

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_COLLECTION")
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")

pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)
vectorstore = PineconeVectorStore.from_existing_index(index_name, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name='gpt-4-turbo',
        temperature=0.0
    ),
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 101})
)

############################################
# Streamlit Chatbot
############################################

import streamlit as st

st.title("Demo: Popsink AS/400 Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = qa.run(prompt)
            st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
