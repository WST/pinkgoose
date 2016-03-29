# -*- coding: utf-8 -*-

# Flask и WTForms
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, StringField, TextAreaField
import wtforms.validators as validators

class LoginForm(Form):
	username = StringField('Имя пользователя', validators = [validators.input_required()])
	password = PasswordField('Пароль')

class PostForm(Form):
	title = StringField(u'Заголовок', validators = [validators.input_required()])
	slug = StringField('URL-имя', validators = [validators.input_required()])
	intro = TextAreaField(u'Вступление', validators = [validators.input_required()])
	fulltext = TextAreaField(u'Полный текст', validators = [validators.input_required()])
