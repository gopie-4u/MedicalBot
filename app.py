from flask import Flask, render_template, jsonify, request 
from src.helper import get_gemini_embeddings
from src.prompt import *
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os 

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Added for Gemini
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

embeddings = get_gemini_embeddings()

index_name = 'medicalvdb'

docsearch = PineconeVectorStore.from_existing_index(index_name=index_name,
                                                     embedding=embeddings)

retriever = docsearch.as_retriever(search_type="similarity",
                                   search_kwargs={"k":3})


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

llm = ChatGroq(model="llama3-70b-8192",temperature=0.4,max_tokens=500)

rag_chain = (
    {
        "context":retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)),
        "input": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke(msg)
    print("Response : ", response)
    return str(response)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8081, debug= True)



