from database.db import db

class RegistrationModel(db.Model):
  __tablename__ = "registrations"

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(100))
  last_name = db.Column(db.String(100))
  birthdate = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(100))
  confirm_password = db.Column(db.String(100))
  country = db.Column(db.String(100))
  state = db.Column(db.String(100))
  city = db.Column(db.String(100))
  neighborhood = db.Column(db.String(100))
  street = db.Column(db.String(100))
  street_number = db.Column(db.String(100))
  card_number = db.Column(db.String(100))
  card_expiration_date = db.Column(db.String(100))
  cvv_code = db.Column(db.String(100))
  cardholder_name = db.Column(db.String(100))

  def __init__(self,
    first_name=None, 
    last_name=None, 
    birthdate=None, 
    email=None, 
    password=None, 
    confirm_password=None, 
    country=None, 
    state=None, 
    city=None, 
    neighborhood=None, 
    street=None, 
    street_number=None, 
    card_number=None, 
    card_expiration_date=None, 
    cvv_code=None, 
    cardholder_name=None
    ) -> None:
      self.first_name = first_name
      self.last_name = last_name
      self.birthdate = birthdate
      self.email = email
      self.password = password
      self.confirm_password = confirm_password
      self.country = country
      self.state = state
      self.city = city
      self.neighborhood = neighborhood
      self.street = street
      self.street_number = street_number
      self.card_number = card_number
      self.card_expiration_date = card_expiration_date
      self.cvv_code = cvv_code
      self.cardholder_name = cardholder_name

  def to_json(self) -> dict:
    return {
      "id": self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "birthdate": self.birthdate,
      "email": self.email,
      "password": self.password,
      "confirm_password": self.confirm_password,
      "country": self.country,
      "state": self.state,
      "city": self.city,
      "neighborhood": self.neighborhood,
      "street": self.street,
      "street_number": self.street_number,
      "card_number": self.card_number,
      "card_expiration_date": self.card_expiration_date,
      "cvv_code": self.cvv_code,
      "cardholder_name": self.cardholder_name
    }