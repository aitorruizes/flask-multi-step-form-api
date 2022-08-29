from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import cross_origin
from models.registration_model import RegistrationModel
from database.db import db

registration_blueprint = Blueprint("registration", __name__)

@registration_blueprint.route("/api/v1/registration", methods=["GET"])
@cross_origin()
def getRegistrationByEmail():
  try:
    email = request.args.get("email")
    
    filteredRegistration = RegistrationModel.query.filter_by(email=email).first()

    return jsonify(RegistrationModel.to_json(filteredRegistration)), 200
  except Exception as exception:
    raise exception

@registration_blueprint.route("/api/v1/registration/step0", methods=["POST"])
@cross_origin()
def createRegistrationOnStep0():
  try:
    first_name = request.json["firstName"]
    last_name = request.json["lastName"]
    birthdate = request.json["birthdate"]
    email = request.json["email"]
    password = request.json["password"]
    confirm_password = request.json["confirmPassword"]

    new_registration = RegistrationModel(
      first_name, 
      last_name, 
      birthdate, 
      email, 
      password, 
      confirm_password
    )

    db.session.add(new_registration)
    db.session.commit()

    return jsonify({}), 201

  except Exception as exception:
    raise exception

@registration_blueprint.route("/api/v1/registration/step1", methods=["PUT"])
@cross_origin()
def updateRegistrationOnStep1():
  try:
    id = request.json["id"]
    country = request.json["country"]
    state = request.json["state"]
    city = request.json["city"]
    neighborhood = request.json["neighborhood"]
    street = request.json["street"]
    street_number = request.json["streetNumber"]

    getRegistration = RegistrationModel.query.filter_by(id=id).first()

    getRegistration.country = country
    getRegistration.state = state
    getRegistration.city = city
    getRegistration.neighborhood = neighborhood
    getRegistration.street = street
    getRegistration.street_number = street_number

    db.session.commit()

    return jsonify(RegistrationModel.to_json(getRegistration)), 200
  except Exception as exception:
    raise exception

@registration_blueprint.route("/api/v1/registration/step2", methods=["PUT"])
@cross_origin()
def updateRegistrationOnStep2():
  try:
    id = request.json["id"]
    card_number = request.json["cardNumber"]
    card_expiration_date = request.json["cardExpirationDate"]
    cvv_code = request.json["cvvCode"]
    cardholder_name = request.json["cardholderName"]

    getRegistration = RegistrationModel.query.filter_by(id=id).first()

    getRegistration.card_number = card_number
    getRegistration.card_expiration_date = card_expiration_date
    getRegistration.cvv_code = cvv_code
    getRegistration.cardholder_name = cardholder_name

    db.session.commit()

    return jsonify(RegistrationModel.to_json(getRegistration)), 200
  except Exception as exception:
    raise exception