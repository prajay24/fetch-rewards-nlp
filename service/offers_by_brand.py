from .data import Data
from .semantic_search import SemanticSearch

data = Data()
semantic_search = SemanticSearch()

class BrandOffers():
    def brand_offers(self, query_brand, is_cosine):

        # get teh data
        brand_results = semantic_search.multiqa_mp_net_semantic_search(query_brand, is_cosine)

        # Sort the dictionary items by their values in descending order
        sorted_results = sorted(brand_results, key=lambda x: x['score'], reverse=True)

        # Get the top 5 results
        top_5_results = sorted_results[:5]

        return top_5_results