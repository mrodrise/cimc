from flask_wtf import Form

from wtforms import TextField, BooleanField, TextAreaField, SubmitField, validators, SelectField
from wtforms.validators import Required


class loginForm(Form):
  email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = TextField("Password", [validators.Required("Please enter a subject.")])
  login = SubmitField("Login")
  register = SubmitField("Register")


class yourHomeForm(Form):
    address = TextField("Address", [validators.Required("Please enter a address.")])
