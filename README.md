# Sanjivani-Medical_Chat_Bot 🩺
## A medical chatbot that can answer questions from a PDF file using Llama2

Sanjivani-Medical_Chat_Bot is a medical chatbot that can answer questions from a PDF file using Llama2, a large language model. It uses data integration, data extraction, text chunking, embedding, semantic indexing, and ranking to process the PDF file and generate answers.


## Features 🚀

- Data integration: It integrates data from multiple sources, such as PDF files, web pages, and databases, to create a unified knowledge base.
- Data extraction: It extracts text from PDF files using OCR (optical character recognition) and NLP (natural language processing) techniques.
- Text chunking: It splits the text into smaller chunks based on sentences, paragraphs, or sections, to reduce the computational complexity and improve the accuracy of the embeddings.
- Embedding: It converts the text chunks and the query into numerical vectors using Llama2, a large language model that can encode semantic and syntactic information.
- Semantic indexing: It creates an index of the embeddings using Pinecone, a vector database that supports fast and scalable similarity search.
- Ranking: It ranks the text chunks based on their similarity to the query embedding and returns the most relevant ones as the ranked result.
- Answer generation: It uses Llama2 again to generate a natural language answer from the ranked result, using the query as the context.