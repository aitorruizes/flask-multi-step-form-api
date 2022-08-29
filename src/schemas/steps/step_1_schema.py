from app import marshmallow
from models.registration_model import RegistrationModel

class Step1Schema(marshmallow.SQLAlchemySchema):
  class Meta:
    model = RegistrationModel

  id = marshmallow.auto_field()
  country = marshmallow.auto_field()
  state = marshmallow.auto_field()
  city = marshmallow.auto_field()
  neighborhood = marshmallow.auto_field()
  street = marshmallow.auto_field()
  street_number = marshmallow.auto_field()

step_1_schema = Step1Schema()