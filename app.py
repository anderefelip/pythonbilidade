from flask import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/difal")
def difal():

    return render_template("difal.html")

@app.route("/icms")
def icms():
    return render_template("icms.html")


@app.route("/cte")
def cte():
    return render_template("cte.html")

if __name__ == '__main__':
   app.run(debug = True)