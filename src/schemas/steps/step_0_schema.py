from app import marshmallow
from models.registration_model import RegistrationModel

class Step0Schema(marshmallow.SQLAlchemySchema):
  class Meta:
    model = RegistrationModel

  first_name = marshmallow.auto_field()
  last_name = marshmallow.auto_field()
  birthdate = marshmallow.auto_field()
  email = marshmallow.auto_field()
  password = marshmallow.auto_field()
  confirm_password = marshmallow.auto_field()