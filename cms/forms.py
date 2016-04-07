# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

# Flask и WTForms
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, StringField, TextAreaField
import wtforms.validators as validators

class CirnoForm(Form):
	def _get_translations(self):
		return CirnoFormTranslations()

class CirnoFormTranslations(object):
	def gettext(self, string):
		messages = {}
		messages['This field is required.'] = 'Это поле обязательно для заполнения'

		if string in messages:
			return messages[string]
		else:
			return string

	def ngettext(self, singular, plural, n):
		return "bar"

class LoginForm(CirnoForm):
	username = StringField('Имя пользователя', validators = [validators.input_required()])
	password = PasswordField('Пароль')

class PostForm(CirnoForm):
	title = StringField(u'Заголовок', validators = [validators.input_required()])
	slug = StringField('URL-имя', validators = [validators.input_required()])
	intro = TextAreaField(u'Вступление', validators = [validators.input_required()])
	fulltext = TextAreaField(u'Полный текст', validators = [validators.input_required()])

class MenuItemForm(CirnoForm):
	title = StringField('Заголовок', validators = [validators.input_required()])
	tooltip = StringField('Подсказка')
