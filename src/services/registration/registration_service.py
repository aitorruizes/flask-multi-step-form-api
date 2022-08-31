from flask import request
from flask import jsonify
from database.db import db
from models.registration.registration_model import RegistrationModel
from schemas.registration.steps.step_0_schema import step_0_schema
from schemas.registration.steps.step_1_schema import step_1_schema
from schemas.registration.steps.step_2_schema import step_2_schema

class RegistrationService():

  def __init__(self) -> None:
    pass

  def createRegistrationOnStep0(self):
    try:
      first_name = request.json["firstName"]
      last_name = request.json["lastName"]
      birthdate = request.json["birthdate"]
      email = request.json["email"]
      password = request.json["password"]
      confirm_password = request.json["confirmPassword"]

      request_body = {
        "first_name": first_name,
        "last_name": last_name,
        "birthdate": birthdate,
        "email": email,
        "password": password,
        "confirm_password": confirm_password
      }

      errors = step_0_schema.validate(request_body)

      if errors:
        return jsonify({ "error": "Missing or incorrect data" }), 400
      else:
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

        return jsonify(step_0_schema.dump(new_registration)), 201
    except Exception as exception:
      raise exception

  def getById(self):
    try:
      email = request.args.get("email")
    
      filteredRegistration = RegistrationModel.query.filter_by(email=email).first()

      return jsonify({ "id": filteredRegistration.id }), 200
    except Exception as exception:
      raise exception

  def updateRegistrationOnStep1(self):
    try:
      id = request.json["id"]
      country = request.json["country"]
      state = request.json["state"]
      city = request.json["city"]
      neighborhood = request.json["neighborhood"]
      street = request.json["street"]
      street_number = request.json["streetNumber"]

      request_body = {
        "country": country,
        "state": state,
        "city": city,
        "neighborhood": neighborhood,
        "street": street,
        "street_number": street_number
      }

      errors = step_1_schema.validate(request_body)

      if errors:
        return jsonify({ "error": "Missing or incorrect data" }), 400
      else:
        filteredRegistration = RegistrationModel.query.filter_by(id=id).first()

        filteredRegistration.country = country
        filteredRegistration.state = state
        filteredRegistration.city = city
        filteredRegistration.neighborhood = neighborhood
        filteredRegistration.street = street
        filteredRegistration.street_number = street_number

        db.session.commit()

        return jsonify(step_1_schema.dump(filteredRegistration)), 200
    except Exception as exception:
      raise exception

  def updateRegistrationOnStep2(self):
    try:
      id = request.json["id"]
      card_number = request.json["cardNumber"]
      card_expiration_date = request.json["cardExpirationDate"]
      cvv_code = request.json["cvvCode"]
      cardholder_name = request.json["cardholderName"]

      request_body = {
        "id": id,
        "card_number": card_number,
        "card_expiration_date": card_expiration_date,
        "cvv_code": cvv_code,
        "cardholder_name": cardholder_name
      }
    
      errors = step_2_schema.validate(request_body)

      if errors:
        return jsonify({ "error": "Missing or incorrect data" }), 400
      else:
        filteredRegistration = RegistrationModel.query.filter_by(id=id).first()

        filteredRegistration.card_number = card_number
        filteredRegistration.card_expiration_date = card_expiration_date
        filteredRegistration.cvv_code = cvv_code
        filteredRegistration.cardholder_name = cardholder_name

        db.session.commit()

        return jsonify(step_2_schema.dump(filteredRegistration)), 200
    except Exception as exception:
      raise exception
    