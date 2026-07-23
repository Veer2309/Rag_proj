import os
import shutil
import tempfile
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Load Environment Variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title="RAG Book Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("RAG Book Assistant")
st.write("Upload a PDF book and ask questions from it.")

# Cache Embedding Model
@st.cache_resource
def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embedding_model = load_embedding_model()

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF Book",
    type="pdf"
)

# Process PDF
if uploaded_file is not None:

    if st.button("Process PDF"):

        with st.spinner("Creating Vector Database..."):

            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                pdf_path = tmp_file.name

            # Delete previous database
            if os.path.exists("chroma_db"):
                shutil.rmtree("chroma_db")

            # Load PDF
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            # Split into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            # Create Chroma DB
            Chroma.from_documents(
                documents=chunks,
                embedding=embedding_model,
                persist_directory="chroma_db"
            )

            os.remove(pdf_path)

        st.success("PDF processed successfully!")

# Ask Questions
if os.path.exists("chroma_db"):

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    llm = ChatMistralAI(
        model="mistral-small-2506"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not found in the context, reply:

'I could not find the answer in the document.'
"""
            ),
            (
                "human",
                """Context:
{context}

Question:
{question}
"""
            )
        ]
    )

    st.divider()

    question = st.text_input("Ask a Question")

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")
        else:

            with st.spinner("Searching..."):

                docs = retriever.invoke(question)

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                final_prompt = prompt.invoke(
                    {
                        "context": context,
                        "question": question
                    }
                )

                response = llm.invoke(final_prompt)

            st.subheader("Answer")
            st.write(response.content)

            with st.expander("Retrieved Context"):
                st.write(context)