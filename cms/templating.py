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

	def render(form):
		hidden_tag = form.hidden_tag()
		controls = [str(field) for field in form if field.widget.input_type != 'hidden']
		return "%s %s" % (hidden_tag, ''.join(controls))

	return {'pony': pony, 'footer_message': footer_message, 'site_title': site_title, 'site_slogan': site_slogan, 'render': render}
