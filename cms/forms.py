# -*- coding: utf-8 -*-

# Flask и WTForms
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, StringField, TextAreaField
import wtforms.validators as validators

class PinkGooseForm(Form):
	def _get_translations(self):
		return MyTranslations()

class MyTranslations(object):
	def gettext(self, string):
		messages = {}
		messages['This field is required.'] = 'Это поле обязательно для заполнения'

		if string in messages:
			return messages[string]
		else:
			return string

	def ngettext(self, singular, plural, n):
		return "bar"

class LoginForm(PinkGooseForm):
	username = StringField('Имя пользователя', validators = [validators.input_required()])
	password = PasswordField('Пароль')

class PostForm(PinkGooseForm):
	title = StringField(u'Заголовок', validators = [validators.input_required()])
	slug = StringField('URL-имя', validators = [validators.input_required()])
	intro = TextAreaField(u'Вступление', validators = [validators.input_required()])
	fulltext = TextAreaField(u'Полный текст', validators = [validators.input_required()])
