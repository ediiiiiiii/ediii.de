from flask import Flask, render_template, request
import json
import random
import orakel
app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template('startseite.html')

@app.route("/zauber/", methods=['GET'])
def zauber():
    return render_template('zauber.html')

@app.route("/bunt/")
def bunt():
    return render_template('bunt.html')

@app.route("/orakel/", methods=['GET', 'POST'])
def orakel_page():
    if request.method == 'POST':
        name = request.json["question"]
        print(name)
        return json.dumps({"response":orakel.evalute(name)})
    elif request.method == 'GET':
        return render_template('orakel.html')

@app.route("/request-coolness/", methods=['GET', 'POST'])
def orakel_anfrage():
    if request.method == 'POST':
        name = request.form.get("name")
        description = request.form.get("description")
        url = "/".join(request.base_url.split("/")[:-2])
        orakel.request_orakel(name, description, url=url)
        return "Hallo"
    elif request.method == 'GET':
        return render_template('orakel_request.html')

@app.route("/accept/<int:id>", methods=['GET'])
def accept(id):
    result = orakel.find_id(id)
    if result:
        name, desc = result
        return render_template('accept.html', id=id, name=name, desc=desc)
    else:
        return render_template('not_found.html')

@app.route("/accept/", methods=['GET'])
def accept_invalid():
    return render_template('not_found.html')

@app.route("/accept/", methods=['POST'])
def accept_post():
    id = request.form.get("id")
    if (orakel.check_request(id)):
        name = request.form.get("name")
        desc = request.form.get("desc")
        orakel.add_user(id, name, desc)
        return "yay"
    else:
        return 404

@app.route("/request-sent/")
def request_sent():
    return render_template('sent.html')

