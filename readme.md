# Popsink AS/400 Chatbot

This repository contains a script to demonstrate a Change Data Capture (CDC) from an AS400 system to Pinecone, using Popsink's platform. It includes a GenAI application demo with a chatbot interface built with Streamlit.

## Features

- Integrates Popsink for CDC from AS400 to Pinecone.
- Uses Pinecone for vector storage and retrieval.
- Utilizes OpenAI's GPT-4 model for chatbot responses.
- Implements a Streamlit interface for an interactive chatbot demo.

## Setup

### Prerequisites

- Python 3.8 or higher
- Pinecone API Key
- OpenAI API Key

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Popsink/popsink-as400-genai.git
    cd popsink-as400-genai
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API keys:

- Rename `config/example.env` to `.env` and update it with your Pinecone and OpenAI API keys as well as Pinecone collection.

    ```env
    PINECONE_API_KEY=your_pinecone_api_key
    OPENAI_API_KEY=your_openai_api_key
    PINECONE_INDEX=your_pinecone_index_name
    ```

### Running the Application

To start the Streamlit chatbot application, run:

```bash
streamlit run main.py
