from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import prompt_template
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Global variables for Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")

# Initialization of Pinecone and Document Search
def initialize_pinecone():
    import pinecone
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    index_name = "med-chatbot"
    embeddings = download_hugging_face_embeddings()
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    return docsearch

docsearch = initialize_pinecone()

# Function to set custom prompt
def set_custom_prompt():
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return prompt

# Function to create a retrieval QA chain
def retrieval_qa_chain(llm, prompt, docsearch):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt},
    )
    return qa_chain

# Function to load the locally downloaded model
def load_llm():
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
    )
    return llm

# QA Model Function
def qa_bot():
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, docsearch)
    return qa

# Output function
def final_result(query):
    print("1. ")
    qa_result = qa_bot()
    print("2. ")
    response = qa_result({'query': query})
    return response

# Flask routes
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    query = request.form["msg"]
    print(query)
    response = final_result(query)
    print("Response: ", response["result"])
    return str(response["result"])

# Run Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
