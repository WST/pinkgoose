# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

from cms.plugins import AbstractCirnoPlugin

class CirnoPlugin(AbstractCirnoPlugin):
	def install(self):
		pass

	def uninstall(self):
		pass

	def menu_item(self, request, item):
		return 'foo'
