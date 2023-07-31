Fetch Rewards - NLP Take Home // Prajay Sachdev (prajay9924@gmail.com)

Steps to run the assignment in a new conda environment

- Create a new conda environment. Use the conda terminal and run the command: 'conda create --name fetch-prajay python=3.8.8'
- Activate 'fetch-prajay' environment
- Launch VSCODE
- Launch Terminal from VSCode, ensure that your conda envirnment is 'fetch-prajay'
- Run the command in the terminal 'pip install -r requirements.txt'. This shall install all the packages required for the project. This may take a few minutes to install
- To activate the server, run, 'uvicorn main:app --reload'
- Ensure there are no other local servers previous running on the same port. Open in an incognito browser window to open 'http://127.0.0.1:8000/docs' This will launch the Swagger Document with the 3 REST APIs


Leveraging NLP Innovations

Semantic search is an advanced search technique that employs natural language processing to understand the contextual meaning behind a user's query, going beyond simple keyword matching. By considering synonyms, related concepts, and the relationship between words, semantic search delivers more accurate and relevant results. It incorporates entity recognition, sentiment analysis, word embeddings, knowledge graphs, and natural language understanding to comprehend user intent better. Implemented in web search engines, digital assistants, and recommendation systems, semantic search significantly enhances user experience by providing contextually precise information and reducing the need for query refinement. Major search engines like Google and Bing have adopted semantic search elements in their algorithms to improve the accuracy and relevance of search results.

SBERT (Sentence-BERT) is a modification of the well-known BERT (Bidirectional Encoder Representations from Transformers) model specifically designed for sentence embeddings. It takes sentences as input and returns fixed-size embeddings that capture the semantic meaning of the sentences.

Semantic search aims to understand the intent behind a query, allowing for more accurate and relevant results. By converting both the query and the documents in a corpus to embeddings using SBERT, it's possible to measure the semantic similarity between them. This is often done by computing the cosine similarity between the query and document embeddings.

'multi-qa-mpnet-base-dot-v1' is a sentence-transformers model: It maps sentences & paragraphs to a 768 dimensional dense vector space and was designed for semantic search. It has been trained on 215M (question, answer) pairs from diverse sources.

I've been exploring the use of the specific SBERT model multi-qa-mpnet-base-dot-v1 for semantic search, and here's how I've found it can be utilized. First, I load this pre-trained model using a library that supports Transformer models. I first loaded this pre-trained model and then I preprocessed the documents, tokenizing and normalizing them before using the SBERT model to create their embeddings. In my approach, I used both cosine similarity (refer to the swagger document with GET APIs starting with /cosine)and dot-product similarity (refer to the swagger document with GET APIs starting with /dot) to compute the similarity scores between the query and document embeddings, allowing for a flexible comparison method. 

I subsequently ranked the documents based on these similarity scores, retrieving the most relevant ones. I found that the multi-qa-mpnet-base-dot-v1 model, possibly tailored for specific semantic search or question-answering tasks, worked effectively for my purposes. 

What could I have done better? 

In my endeavor to enhance semantic search capabilities, I considered employing multi-task learning with RoBERTa to augment the existing multi-qa-mpnet-base-dot-v1 SBERT model. By integrating RoBERTa's superior contextual embeddings, and devising a multi-task learning framework to simultaneously train on various related tasks such as question-answering, sentence similarity, and clustering, I aimed to enable the model to share insights across tasks for better generalization and robustness. This would involve leveraging RoBERTa's well-tuned hyperparameters, implementing a shared encoder for knowledge transfer, and exploring fine-tuning strategies to balance specialization and generalization. I also contemplated experimenting with both cosine similarity and dot-product similarity measures and conducting extensive evaluations for continuous refinements. Through these strategic enhancements, I believed that the integration of RoBERTa and a multi-task learning approach could have potentially led to a more nuanced and adaptive model for semantic search, offering a deeper understanding of textual relationships and advancing the state-of-the-art in semantic search technologies.