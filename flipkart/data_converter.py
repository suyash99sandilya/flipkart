import pandas as pd
from langchain.schema import Document  # Corrected import for Document

def dataconverter():
    # Read the product data from the CSV file
    product_data = pd.read_csv("data/flipkart_product_review.csv")
    
    # Extract relevant columns
    data = product_data[["product_title", "review"]]
    
    # Initialize a list to store product data
    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        product = {
            "product_name": row["product_title"],
            "review": row["review"]
        }
        # Append the product object to the list
        product_list.append(product)

    # Initialize a list to store documents
    docs = []

    # Convert each product object into a Document
    for product in product_list:
        metadata = {"product_name": product["product_name"]}
        page_content = product["review"]

        # Create a Document and append it to the list
        doc = Document(page_content=page_content, metadata=metadata)
        docs.append(doc)

    return docs
