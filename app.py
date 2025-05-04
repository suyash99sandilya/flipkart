from flask import Flask, render_template, request
from flipkart.retrieval_generation import generation
from flipkart.data_ingestion import data_ingestion


vstore = data_ingestion("done")
chain = generation(vstore)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #1st page of my chatbot



@app.route("/get", methods = ["POST", "GET"]) #page for QA
def chat():
   
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "suyash"}
    },
)["answer"]

      return str(result)

if __name__ == '__main__': #calling my flask app
    
    app.run(host="0.0.0.0", port=5000, debug= True)