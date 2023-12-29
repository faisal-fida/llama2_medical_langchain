# Sanjivani-Medical_Chat_Bot 🩺
## A medical chatbot that can answer questions from a PDF file using Llama2

Sanjivani-Medical_Chat_Bot is a medical chatbot that can answer questions from a PDF file using Llama2, a large language model. It uses data integration, data extraction, text chunking, embedding, semantic indexing, and ranking to process the PDF file and generate answers.


## ⚙️ Tech Stack

This project is built using the following technologies:

- **Python**: The backbone of the project. All the scripts are written in Python.
- **Langchain**: A package used for generating and evaluating quizzes.
- **Flask**: A Python library used to create the web interface for the application.
- **LLM Model**: Meta Llama2.
- **Quantized Model**: llama-2-7b-chat.ggmlv3.q4_0.bin
- **Vector DataBase**: Pinecone
- **PDF File**: The gale encyclopedia of medicine second edition vol 1


## Features 🚀

- **Data integration:** It integrates data from multiple PDF files to create a unified knowledge base.
- **Data extraction:** It extracts text from PDF files using OCR (optical character recognition) and NLP (natural language processing) techniques.
- **Text chunking:** It splits the text into smaller chunks based on sentences, paragraphs, or sections, to reduce the computational complexity and improve the accuracy of the embeddings.
- **Embedding:** It converts the text chunks and the query into numerical vectors using Llama2, a large language model that can encode semantic and syntactic information.
- **Semantic indexing:** It creates an index of the embeddings using Pinecone, a vector database that supports fast and scalable similarity search.
- **Ranking:** It ranks the text chunks based on their similarity to the query embedding and returns the most relevant ones as the ranked result.
- **Answer generation:** It uses Llama2 again to generate a natural language answer from the ranked result, using the query as the context.


## Installation 💻

To install and run this project, you need to have Python 3.9 or higher and pip installed on your system. You also need to have an API key for Pinecone and a PDF file (medical book) as the data source.

Follow these steps to install and run this project:

### 1. Clone this repository to your local machine using:
```bash
git clone https://github.com/Prashantkhobragade/Sanjivani-Medical_Chat_Bot.git
```

### 2. Create a conda environment after opening the repository:
```bash
conda create -n mchat python=3.9 -y
```
```bash
conda activate mchat/
```
### 3. Install the requirements:
```bash
pip install -r requirements.txt
```

### 4. Create a .env file in the root directory and add your Pinecone credentials as follows:
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
### 5. Download the quantized model from the link and keep the model in the model directory:
```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
### 6. Uncomment the #initializing the Pinecone block code and run the following command:
```ini
python store_index.py
```
### 7. finally
```ini
python app.py
```

## Usage 📝

To use this project, you need to enter a natural language query related to the PDF file (medical book) that you have provided as the data source. The project will then process the query and the PDF file and generate an answer for you.

For example, if you have a PDF file about diabetes, you can enter a query like "What is the treatment for diabetes?" and the project will generate an answer like "The treatment for diabetes depends on the type, severity, and other factors. Some common treatments include diet, exercise, medication, and insulin therapy."

## Contributing 🙌

This project is open for contributions from anyone interested in medical chatbots or Llama2. Here are some ways you can contribute:

- Report bugs, suggest features, or ask questions by opening an issue.
- Fork the repository, make changes, and submit a pull request.


## References 📚

This project is based on the following papers and resources:

- [Llama2: A Large Language Model for Answering Questions](https://ai.meta.com/llama/)
- [Pinecone: A Vector Database for Machine Learning](https://www.pinecone.io/learn/vector-database/)
