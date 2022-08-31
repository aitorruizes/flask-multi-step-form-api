from flask import Blueprint
from flask_cors import cross_origin
from services.registration.registration_service import RegistrationService

registration_blueprint = Blueprint("registration", __name__)
registration_service = RegistrationService()

@registration_blueprint.route("/api/v1/registration", methods=["GET"])
@cross_origin()
def getRegistrationIdByEmail():
  return registration_service.getById()

@registration_blueprint.route("/api/v1/registration/step0", methods=["POST"])
@cross_origin()
def createRegistrationOnStep0():
  return registration_service.createRegistrationOnStep0()

@registration_blueprint.route("/api/v1/registration/step1", methods=["PUT"])
@cross_origin()
def updateRegistrationOnStep1():
  return registration_service.updateRegistrationOnStep1()

@registration_blueprint.route("/api/v1/registration/step2", methods=["PUT"])
@cross_origin()
def updateRegistrationOnStep2():
  return registration_service.updateRegistrationOnStep2()