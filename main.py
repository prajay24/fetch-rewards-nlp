from fastapi import FastAPI

from service import offers_by_brand, offers_by_categories, offers_by_retailer
BrandOffers = offers_by_brand.BrandOffers()
CategoryOffers = offers_by_categories.CategoryOffers()
RetailerOffers = offers_by_retailer.RetailerOffers()

app = FastAPI(title = "Fetch Rewards-NLP")

@app.get("/")
async def my_first_get_api():
    return {"hello":"hello world!"}

# cosine similarity
@app.get("/cosine/offer/brand/{brand_name}") 
async def get_brand_offers_cosine(brand_name:str):

    if brand_name is None:
        return {"error":"brand name is missing"}
    
    return BrandOffers.brand_offers(brand_name, True)

@app.get("/cosine/offer/retailer/{retailer_name}") 
async def get_retailer_offers_cosine(retailer_name:str):

    if retailer_name is None:
        return {"error":"retailer name is missing"}
    
    return RetailerOffers.retailer_offers(retailer_name, True)

@app.get("/cosine/offer/category/{category_name}") 
async def get_category_offers_cosine(category_name:str):

    if category_name is None:
        return {"error":"category name is missing"}
    
    return CategoryOffers.category_offers(category_name, True)

# dot score
@app.get("/dot/offer/brand/{brand_name}") 
async def get_brand_offers_dot(brand_name:str):

    if brand_name is None:
        return {"error":"brand name is missing"}
    
    return BrandOffers.brand_offers(brand_name, False)

@app.get("/dot/offer/retailer/{retailer_name}") 
async def get_retailer_offers_dot(retailer_name:str):

    if retailer_name is None:
        return {"error":"retailer name is missing"}
    
    return RetailerOffers.retailer_offers(retailer_name, False)

@app.get("/dot/offer/category/{category_name}") 
async def get_category_offers_dot(category_name:str):

    if category_name is None:
        return {"error":"category name is missing"}
    
    return CategoryOffers.category_offers(category_name, False)