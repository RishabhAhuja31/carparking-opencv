from app import app
from model.user_model import user_model
from flask import request
from flask_cors import CORS
from subprocess import call
import QRScanner.webcam
obj=user_model()
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    print(request.form)
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    print(request.form)
    return obj.user_update_model(request.form)

@app.route("/user/balance", methods=["PUT"])
def user_balance_controller():
    print(request.form)

    return obj.user_balance_model(request.form)

@app.route("/user/class", methods=["PATCH"])
def user_class_controller():
    print(request.form)
    return obj.user_class_model(request.form,id)

