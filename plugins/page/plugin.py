# -*- coding: utf-8 -*-

from cms.plugins import AbstractCirnoPlugin

class CirnoPlugin(AbstractCirnoPlugin):
	def install(self):
		pass

	def uninstall(self):
		pass

	def menu_item(self, request, item):
		return 'foo'
