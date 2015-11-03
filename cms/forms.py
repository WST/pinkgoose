# -*- coding: utf-8 -*-

# Flask и WTForms
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
	username = TextField('username', validators = [Required()])
	password = PasswordField('password')
