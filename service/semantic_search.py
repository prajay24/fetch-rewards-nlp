from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
from .data import Data

data = Data()

class SemanticSearch():

    def multiqa_mp_net_semantic_search(self, query, is_cosine):
            # Initialize the model
            model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

            documents = data.data_for_semantic()

            # Encode the documents and query
            doc_embeddings = model.encode(documents)
            query_embedding = model.encode([query])

            # Compute cosine similarity between the query and all documents
            similarities = None
            if is_cosine:
                similarities = cosine_similarity(query_embedding, doc_embeddings)
            else:
                similarities = util.dot_score(query_embedding, doc_embeddings).cpu().tolist()

            similarity_list = []
            for doc, score in zip(documents, similarities[0]):
                index = doc.find("/////")
                if index != -1:
                    result = doc[:index]
                else:
                    result = doc
                
                if is_cosine:
                    similarity_list.append({"offer": result, "score": round(score * 100, 2)})
                else:
                    similarity_list.append({"offer": result, "score": score})
                
            # Return the dictionary
            return similarity_list
    
    