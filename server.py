from flask import Flask, render_template, request, url_for, flash, redirect
from healthchainblockchain import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/input", methods=('GET', 'POST'))
def add_information():
    if request.method == "POST":
        info_type = request.form["subject"]
        patient_name = request.form["uname"]
        bday = request.form["bday"]
        state = request.form["state"]

        # process information

        return redirect(url_for("input"))
        
    return render_template("organINPUT.html")

@app.route("/obtain", methods=('GET', 'POST'))
def obtain_information():
    if request.method == "POST":
        secret_key = request.form("key")

    return render_template("organOBTAINDATA.html")



if __name__=="__main__":

    pubkey, privkey = get_keys()
    print(pubkey, privkey)


    app.run()