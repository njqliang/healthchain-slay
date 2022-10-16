from flask import Flask, render_template, request, url_for, redirect
from healthchainblockchain import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("HOMEPAGE.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/input", methods=('GET', 'POST'))
def add_information():
    if request.method == "POST":
        info_type = request.form["subject"]
        patient_name = request.form["uname"]
        bday = request.form["bday"]
        state = request.form["state"]
        city = request.form["city"]
        opo = request.form["opo"]
        pname = request.form["pname"]
        blood = request.form["blood"]
        organ = request.form["organ"]
        organsize = request.form["organsize"]
        notes = request.form["notes"]

        pubkey = request.form["pubkey"]

        all_info = " ".join([info_type, patient_name, bday, state, city, opo, pname, blood, organ, organsize, notes])
        add_to_chain(all_info, pubkey)

        return redirect("/")
        
    return render_template("organINPUT.html")

@app.route("/obtain", methods=('GET', 'POST'))
def obtain_information():
    if request.method == "POST":
        secret_key = request.form["privkey"]

        findings = read_chain(secret_key)

        print(findings)

        return render_template("results.html", len = len(findings), results=findings)

    return render_template("organOBTAINDATA.html")



if __name__=="__main__":

    # pubkey, privkey = get_keys()
    # print(pubkey, privkey)

    app.run(host='127.0.0.1')