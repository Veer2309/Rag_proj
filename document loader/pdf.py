from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader(
    "document loader/Artificial Intelligence, Machine Learning, and Deep Learning.pdf"
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter. split_documents (docs)

print(chunks[6].page_content)