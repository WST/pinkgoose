# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

# Наше приложение
from cms import site

# Python
import random

@site.application.context_processor
def preprocess_context():
	pony = random.choice(site.application.config['PONIES'])
	footer_message = random.choice(site.application.config['FOOTER_MESSAGES'])
	site_title = site.application.config['SITE_TITLE']
	site_slogan = site.application.config['SITE_SLOGAN']

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
		controls = "<div class=\"form-controls\"><button type=\"submit\" class=\"btn\" />%s</button></div>" % submit_caption
		return "<form method=\"post\">%s<table>%s</table>%s</form>" % (hidden_tag, ''.join(widgets), controls)

	def post_url(post):
		return '/posts/%s' % post['slug']

	def render_menu(menu):
		result = '<ul>'
		for item in menu:
			if 'children' in item and len(item['children']) > 0:
				result += "<li><a href=\"%s\" title=\"%s\">%s</a>%s</li>" % (item['url'], item['tooltip'], item['title'], render_menu(item['children']))
			else:
				result += "<li><a href=\"%s\" title=\"%s\">%s</a></li>" % (item['url'], item['tooltip'], item['title'])

		result += '</ul>'
		return result

	return {
		'pony': pony,
		'footer_message': footer_message,
		'site_title': site_title,
		'site_slogan': site_slogan,
		'render': render,
		'post_url': post_url,
		'menu': site.structure,
		'render_menu': render_menu,
	}
