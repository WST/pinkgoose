# -*- coding: utf-8 -*-

# Наше приложение
from cms import application

# Flask
from flask import current_app

# Python
import random

@application.context_processor
def preprocess_context():
	pony = random.choice(current_app.config['PONIES'])
	footer_message = random.choice(current_app.config['FOOTER_MESSAGES'])
	site_title = current_app.config['SITE_TITLE']
	site_slogan = current_app.config['SITE_SLOGAN']

	def visible(field):
		try:
			return field.widget.input_type != 'hidden'
		except:
			return True

	def field_row(field, errors):
		if field.name in errors:
			error = '<br />'.join(errors[field.name])
			return "<tr class=\"field-error\"><td width=\"180\">%s</td><td>%s<br/><span class=\"field-error\">%s</span></td></tr>" % (field.label(), str(field), error)
		else:
			return "<tr><td>%s:</td><td>%s</td></tr>" % (field.label(), str(field))

	def render(form, submit_caption = 'Сохранить'):
		hidden_tag = form.hidden_tag()
		widgets = [field_row(field, form.errors) for field in form if visible(field)]
		controls = "<div class=\"form-controls\"><input type=\"submit\" value=\"%s\" /></div>" % submit_caption
		return "<form method=\"post\">%s<table>%s</table>%s</form>" % (hidden_tag, ''.join(widgets), controls)

	return {'pony': pony, 'footer_message': footer_message, 'site_title': site_title, 'site_slogan': site_slogan, 'render': render}
