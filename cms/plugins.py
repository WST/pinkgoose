# -*- coding: utf-8 -*-

class AbstractCirnoPlugin:
	def __init__(self, site):
		self.site = site
		self.name = type(self).__module__.split('.')[0]
		print("Initializing plugin: %s" % self.name)
