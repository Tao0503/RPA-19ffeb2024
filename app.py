from flask import Flask,request,render_template
import replicate
import os
import time
from openai import OpenAI

app = Flask(__name__)

r = ""
first_time = 1

@app.route("/main",methods=["GET","POST"])
def main():
    global r,first_time
    if first_time==1:
        r = request.form.get("r")
        first_time=0
    return(render_template("main.html",r=r))
    
@app.route("/about_mrs_huang", methods=["GET", "POST"])
def about_mrs_huang():
    return render_template("about_mrs_huang.html")

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/end",methods=["GET","POST"])
def end():
    global first_time
    first_time = 1
    return(render_template("end.html"))


if __name__ == "__main__":
    app.run()
