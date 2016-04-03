# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

# Cirno
from cms.plugins import AbstractCirnoPlugin

# Flask
from flask import render_template, url_for

class CirnoPlugin(AbstractCirnoPlugin):
	def install(self):
		pass

	def uninstall(self):
		pass

	def menu_item(self, request, item):
		return render_template('static-page.htt', title = '', item = item)
