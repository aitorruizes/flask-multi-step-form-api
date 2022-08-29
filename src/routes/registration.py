from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import cross_origin
from models.registration_model import RegistrationModel
from database.db import db
from schemas.steps.step_0_schema import Step0Schema
from schemas.steps.step_1_schema import Step1Schema
from schemas.steps.step_2_schema import Step2Schema

registration_blueprint = Blueprint("registration", __name__)

@registration_blueprint.route("/api/v1/registration", methods=["GET"])
@cross_origin()
def getRegistrationIdByEmail():
  try:
    email = request.args.get("email")
    print(email)
    
    filteredRegistration = RegistrationModel.query.filter_by(email=email).first()

    return jsonify({ "id": filteredRegistration.id }), 200
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

    step_0_schema = Step0Schema()

    return jsonify(step_0_schema.dump(new_registration)), 201
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

    filteredRegistration = RegistrationModel.query.filter_by(id=id).first()

    filteredRegistration.country = country
    filteredRegistration.state = state
    filteredRegistration.city = city
    filteredRegistration.neighborhood = neighborhood
    filteredRegistration.street = street
    filteredRegistration.street_number = street_number

    db.session.commit()

    step_1_schema = Step1Schema()

    return jsonify(step_1_schema.dump(filteredRegistration)), 200
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

    filteredRegistration = RegistrationModel.query.filter_by(id=id).first()

    filteredRegistration.card_number = card_number
    filteredRegistration.card_expiration_date = card_expiration_date
    filteredRegistration.cvv_code = cvv_code
    filteredRegistration.cardholder_name = cardholder_name

    db.session.commit()

    step_2_schema = Step2Schema()

    return jsonify(step_2_schema.dump(filteredRegistration)), 200
  except Exception as exception:
    raise exception