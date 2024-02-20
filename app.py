from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/imageGPT",methods=["GET","POST"])
def main():
  r = request.form.get("r")
  return(render_template("imageGPT.html",r=r))

if __name__ == "__main__":
         app.run()