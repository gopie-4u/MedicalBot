from src.helper import load_pdf_file, text_split, get_gemini_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file(data="Data/" )
text_chunks = text_split(extracted_data)
embeddings = get_gemini_embeddings()

# Pinecone object creation

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalvdb"

index_list = pc.list_indexes().names()

if index_name not in index_list:
    pc.create_index(name=index_name,
                    dimension=768,
                    metric='cosine',
                    spec = ServerlessSpec(cloud="aws",
                                          region="us-east-1"))
    
# Embed and upsert into Pine cone
docsearch = PineconeVectorStore.from_documents(documents=text_chunks,
                                   embedding=embeddings,
                                   index_name=index_name)