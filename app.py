from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")

pinecone.init(api_key=PINECONE_API_KEY,environment=PINECONE_API_ENV)

index_name = "med-chatbot"
embeddings = download_hugging_face_embeddings()
docsearch = Pinecone.from_existing_index(index_name, embeddings)


def set_custom_prompt():    
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=prompt_template,
                        input_variables=["context","question"])
    return prompt


def retrieval_qa_chain(llm, prompt, docsearch):
    """
    Retrieval QA Chain
    """
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt},
        )
    return qa_chain


def load_llm():
    """
    Load the locally downloaded model here
    """
    llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5,
    )
    return llm


def qa_bot(index_name: str):
    """
    QA Model Function
    """
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, docsearch)
    return qa


def final_result(query):
    """
    Output function
    """
    print("1. ")
    qa_result = qa_bot(index_name)
    print("2. ")
    response = qa_result({'query': query})
    return response


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    query = request.form["msg"]
    print(query)
    response = final_result(query)
    print("Response : ", response["result"])
    return str(response["result"])

    
if __name__ == '__main__':
    app.run(debug=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug= True)