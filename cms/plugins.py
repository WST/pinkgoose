# -*- coding: utf-8 -*-

from cms import site

class AbstractCirnoPlugin:
	def __init__(self, site):
		self.site = site
		self.name = type(self).__module__.split('.')[0]
		print("Initializing plugin: %s" % self.name)
