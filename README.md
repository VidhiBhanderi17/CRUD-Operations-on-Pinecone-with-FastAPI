# CRUD-Operations-on-Pinecone-with-FastAPI

This project demonstrates how to integrate Pinecone with FastAPI and OpenAI to create, update, delete, and query vector embeddings.

## Overview

### Pinecone
Pinecone is a vector database designed to enable fast and scalable search and retrieval of high-dimensional vectors. It is commonly used for applications such as semantic search, recommendation systems, and machine learning model inference.

### FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to be easy to use and to provide automatic interactive API documentation.

### OpenAI
OpenAI provides various state-of-the-art AI models that can generate embeddings from text, which can then be stored in Pinecone for efficient retrieval.

## Project Structure

Project/
├── .env
├── main.py
├── requirements.txt
└── README.md

### Files and Directories

- `.env`: Contains environment variables for Pinecone and OpenAI API keys.
- `main.py`: The main FastAPI application.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: This file, which provides project instructions and documentation.

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package installer)
- Pinecone and OpenAI API keys

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:

    Create a `.env` file in the root of your project and add your Pinecone and OpenAI API keys:
    ```plaintext
    PINECONE_API_KEY=your-pinecone-api-key
    OPENAI_API_KEY=your-openai-api-key
    PINECONE_CLOUD=aws
    PINECONE_REGION=us-east-1
    ```

### Running the Application

1. **Run the FastAPI application**:

    ```bash
    python -m uvicorn main:app --reload
    ```

2. **Access the API documentation**:

    Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation provided by FastAPI.

## API Endpoints

- `POST /insert/`: Insert data into Pinecone.
- `POST /update/`: Update existing data in Pinecone.
- `POST /delete/`: Delete data from Pinecone.
- `POST /retrieve/`: Retrieve the top 5 most similar results based on a query.


