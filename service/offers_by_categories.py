from .data import Data
from .semantic_search import SemanticSearch
import pandas as pd

data = Data()
semantic_search = SemanticSearch()

class CategoryOffers():
    def category_search_items(self, query_category):
        
        grouped_categories = data.list_of_categories()
        search_items = []
        # check if the category is a parent category or not
        if query_category in set(grouped_categories['product_category'].tolist()):

            # Find the response for the user input
            response_str = grouped_categories.loc[grouped_categories['product_category'].str.lower() == query_category.lower(), 'sister_products'].values[0]

            # Convert the response string to an array
            search_items = response_str.split(', ')

        else:
            search_items.append(query_category)

        return search_items   

    def top_5_results_for_item(self, item, is_cosine):
        search_category_offers = semantic_search.multiqa_mp_net_semantic_search(item, is_cosine)
        sorted_results = sorted(search_category_offers, key=lambda x: x['score'], reverse=True)
        sorted_results = sorted_results[:5]

        return sorted_results

    def category_offers(self,query_category, is_cosine):

        return_suggestions = []
        for item in self.category_search_items(query_category):
            item_dict = dict()
            item_dict["item"] = item
            item_dict["offers"] = self.top_5_results_for_item(item, is_cosine)
            return_suggestions.append(item_dict)

        return return_suggestions