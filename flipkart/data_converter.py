import pandas as pd
from langchain core.documents import Document # type: ignore

def dataconverter():
    product_data = pd.read_csv("data\\flipkart_product_review.csv")

    data = product_data[["product_title","review"]]

    product_list =[]


## Itrate over the rows of the DataFrame

for index, row in data.iterrows(): # type: ignore
  object = {
      "product_name": row["product_title"],
      "review": row["review"]
  }

  ## Append the object to the product list

  product_list.append(object)

  docs = []

for object in product_list:
  metadata = {"product_name": object["product_name"]}
  page_content = object["review"]

  doc = Document(page_content= page_content, metadata= metadata)

  docs.append(doc) 
return docs