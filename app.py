import requests
from flask import Flask,render_template,url_for
from flask import request as req

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def Index():
     return render_template('index.html')

@app.route('/MetDet',methods=["GET","POST"])
def MetDet():
     if req.method=="POST":
          API_URL = "https://api-inference.huggingface.co/models/lwachowiak/Metaphor-Detection-XLMR"
          headers = {"Authorization": "Bearer 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"}

          data= req.form["data"]

          def query(payload):
               response = requests.post(API_URL, headers=headers, json=payload)
               return response.json()
               
          output = query({
               "inputs": data,
               #"parameters":{"aggregation_strategy"},
          })

          return render_template("index.html",result=output)
     else:
          return render_template('index.html')

@app.route('/index.html')
def home():
     return render_template('index.html')

@app.route('/services.html')
def services():
     return render_template('services.html')

@app.route('/textsum.html',methods=["GET","POST"])
def Textsum():
     return render_template("textsum.html") 

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
     if req.method== "POST":
          API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
          headers = {"Authorization": "Bearer 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"}

          data = req.form["data"]

          maxL=int(req.form["maxL"])
          minL=maxL//4
          def query(payload):
               response = requests.post(API_URL, headers=headers, json=payload)
               return response.json()
          output = query({
               "inputs": data,
               "parameters":{"min_length":minL,"max_length":maxL},
            })[0]
          
          return render_template('textsum.html', result=output["summary_text"])
     else:
          return render_template('textsum.html')

@app.route('/contact.html')
def contact():
     return render_template('contact.html')

@app.route('/about.html')
def about():
     return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run