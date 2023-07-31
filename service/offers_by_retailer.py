from .data import Data
from .semantic_search import SemanticSearch

data = Data()
semantic_search = SemanticSearch()

class RetailerOffers():
    def retailer_offers(self, query_retailer, is_cosine):

        retailer_results = semantic_search.multiqa_mp_net_semantic_search(query_retailer, is_cosine)

        # Sort the dictionary items by their values in descending order
        sorted_results = sorted(retailer_results, key=lambda x: x['score'], reverse=True)

        # Get the top 5 results
        top_5_results = sorted_results[:5]

        return top_5_results