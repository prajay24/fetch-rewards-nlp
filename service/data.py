import pandas as pd
class Data:
    def data_for_semantic(self):
        # brand_category = pd.read_csv('research/brand_category.csv')
        # categories = pd.read_csv('research/categories.csv')
        offer_retailer = pd.read_csv('data/offer_retailer.csv')

        # fill na with ""
        offer_retailer['RETAILER'] = offer_retailer['RETAILER'].fillna('')

        # creating a lookup column for brand
        offer_retailer["brand_lookup"] = offer_retailer["OFFER"] + " ///// " + offer_retailer["RETAILER"] + " " + offer_retailer["BRAND"]

        return offer_retailer["brand_lookup"].tolist()

    def list_of_categories(self):

        categories = pd.read_csv('data/categories.csv')

        # New dataframe to store the results
        new_categories = pd.DataFrame(columns=["product_category", "sister_products"])

        # Group by parent category and combine sister products
        for parent_category, group in categories.groupby("IS_CHILD_CATEGORY_TO"):
            sister_products = ", ".join(group["PRODUCT_CATEGORY"])
            new_categories = new_categories.append({"product_category": parent_category, "sister_products": sister_products}, ignore_index=True)

        return new_categories

            
        
