from flask import Flask, jsonify, request as req
from flask_cors import CORS
from moonstar.app.signUp.signUp import SignUp as sign
from moonstar.app.login.login import Login as login
from moonstar.app.gachya.gachya import Gachya as gch

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "*"}})

@app.route("/check-id", methods = ['POST'])
def sign_up():
    user = req.json
    return jsonify(sign.check_id(user))
    
@app.route("/check-nick", methods = ['POST'])
def check_nickname():
    user = req.json
    return jsonify(sign.check_nick(user))

@app.route('/check-email', methods = ['POST'])
def check_email():
    user = req.json
    return jsonify(sign.check_email(user))

@app.route('/sign-up', methods=['POST'])
def signUp():
    user = req.json
    return jsonify(sign.sign_up(user))

@app.route('/login', methods=['POST'])
def logins():
    user = req.json
    return jsonify(login.check_login(user))

@app.route('/gachya', methods=['POST'])
def gachya():
    a_type = req.json
    return jsonify(gch.per_gachya(a_type))