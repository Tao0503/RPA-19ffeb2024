from flask import Flask,request,render_template
import replicate
import os

app = Flask(__name__)
os.environ["REPLICATE_API_TOKEN"]="r8_STBS634px9hv4QKE4KsosC44Jk5Roqn2MRG5v"
r = ""
first_time = 1

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global r,first_time
    if first_time==1:
        r = request.form.get("r")
        first_time=0
    return(render_template("main.html",r=r))
@app.route("/image_gpt",methods=["GET","POST"])
def image_gpt():
    return(render_template(i="image_gpt.html"))
@app.route("/image_result",methods=["GET","POST"])
def image_result():
    q = request.form.fet("q")
    r = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={
        "prompt": q,
        }
    )
    time.sleep(10)
    return(render_template(i="image_result.html",r=r[0]))
    
@app.route("/end",methods=["GET","POST"])
def end():
  return(render_template("image_gpt.html"))

if __name__ == "__main__":
    app.run()


