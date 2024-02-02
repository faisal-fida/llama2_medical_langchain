## Llama-Medical_Chat_Bot: Q&A from Medical PDFs with Llama2

**Answer medical questions directly from a PDF** using Llama2, a powerful language model. This Python project leverages data integration, embedding, and semantic indexing to deliver accurate and relevant answers.

**Key Features:**

* **Data Extraction:** Extracts text from PDFs using OCR and NLP.
* **Embedding & Indexing:** Converts text and queries into efficient vectors for fast search.
* **Answer Generation:** Employs Llama2 to craft natural language responses.

**Tech Stack:**

* Python
* Langchain
* Flask
* Llama2 (Meta)
* Pinecone Vector Database

**Getting Started:**

1. **Clone this Repository**
2. **Setup Environment:** Create a Python 3.9 conda environment (instructions provided).
3. **Install Dependencies:** `pip install -r requirements.txt`
4. **Configure Pinecone:** Add API key and environment to a `.env` file.
5. **Download & Store Model:** Download the quantized Llama2 model and initialize Pinecone index.
6. **Run Application:** `python app.py`

**Usage:**

Enter a natural language query related to your medical PDF. The chatbot will process the query and PDF, returning a relevant answer.

**References:**

* Llama2
* Pinecone
