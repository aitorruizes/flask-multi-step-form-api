from app import marshmallow
from models.registration_model import RegistrationModel

class Step2Schema(marshmallow.SQLAlchemySchema):
  class Meta:
    model = RegistrationModel

  card_number = marshmallow.auto_field()
  card_expiration_date = marshmallow.auto_field()
  cvv_code = marshmallow.auto_field()
  cardholder_name = marshmallow.auto_field()