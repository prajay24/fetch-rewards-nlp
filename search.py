
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import scipy

# Load the SBERT model
embedder = SentenceTransformer('bert-base-nli-mean-tokens')

# Function to perform the search and return results
def search(input_str, query):
    closest_n = st.slider("Number of closest sentences to display", min_value=5, max_value=50, value=8, step=5)
    query_embeddings = embedder.encode([query])
    corpus_embeddings = embedder.encode(input_str)
    distances = scipy.spatial.distance.cdist(query_embeddings, corpus_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])

    results_list = []
    for idx, distance in results[0:closest_n]:
        result = {}
        result['sentence'] = input_str[idx].strip()
        result['cosine_similarity'] = (1 - distance)
        results_list.append(result)

    return results_list
 
# Streamlit interface
def main():
    st.set_page_config(page_title="Semantic Search Engine", page_icon=":mag_right:", layout="wide")
    st.title("Semantic Search Engine with SBERT")

    # uploaded_file = st.file_uploader("Upload your CSV data file", type=["csv"])
    # if uploaded_file is not None:
    #     df = pd.read_csv(uploaded_file)
    #     query = st.text_input("Enter your search query")
    #     if st.button("Search"):
    #         results = search(df, query)
    #         st.write("Results:", len(results))
    #         st.dataframe(pd.DataFrame(results))




if __name__ == '__main__':
    main()