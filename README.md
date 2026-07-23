# 📄 RAG-Based Document Question Answering System

A Retrieval-Augmented Generation (RAG) application that allows users to upload their own PDF documents and ask questions about their content using **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, **Mistral AI**, and **Streamlit**.

---

## Features

* Upload any PDF document
* Automatically split the document into chunks
* Generate semantic embeddings using Hugging Face
* Store embeddings in ChromaDB
* Retrieve the most relevant context
* Generate accurate, context-aware responses using Mistral AI
* Simple and interactive Streamlit interface

---

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers
* Mistral AI
* PyPDF

---

## Project Structure

```text
Rag_proj/
│
├── app.py                  # Streamlit application
├── create_database.py      # Creates the vector database
├── main.py                 # Terminal-based chatbot (optional)
├── requirements.txt
├── chroma_db/              # Generated vector database
├── uploads/                # Uploaded PDFs
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Example:

```bash
git clone https://github.com/your-username/Rag_proj.git
```

---

## 2. Navigate to the Project

```bash
cd Rag_proj
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure the Mistral API Key

Create a file named:

```text
.env
```

Add the following:

```env
MISTRAL_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Mistral API key.

---

## 6. Run the Application

```bash
streamlit run app.py
```

After running the command, Streamlit will automatically open the application in your browser.

If it doesn't, open:

```text
http://localhost:8501
```

---

# How to Use

### Step 1

Launch the Streamlit application.

---

### Step 2

Upload a PDF document.

---

### Step 3

Click **Process PDF**.

The application will:

* Read the PDF
* Split it into text chunks
* Generate embeddings
* Store them in ChromaDB

---

### Step 4

Enter your question in the text box.

Example:

> What are the eligibility criteria?

---

### Step 5

Click **Get Answer**.

The chatbot retrieves the most relevant document chunks and generates an answer using Mistral AI.

---

# How It Works

```text
PDF
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Hugging Face Embeddings
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Retriever
      │
      ▼
Mistral AI
      │
      ▼
Answer
```

---

# Notes

* Only PDF documents are currently supported.
* A valid Mistral API key is required.
* The vector database is generated automatically after processing a document.
* Reprocessing a new PDF replaces the previous vector database.

---

# Future Improvements

* Support for multiple PDFs
* Chat history
* Source citations
* Support for DOCX and TXT files
* Conversation memory
* Deploy on Streamlit Cloud

---

# License

This project is intended for educational and learning purposes.
