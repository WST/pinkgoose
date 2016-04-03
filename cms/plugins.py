# -*- coding: utf-8 -*-

# Python
import os

# Cirno
from cms import site
from cms.site import TEMPLATE_ROOT, PLUGIN_ROOT

class AbstractCirnoPlugin:
	template_loader = None
	template_env = None

	def __init__(self, site):
		self.site = site
		self.name = type(self).__module__.split('.')[0]
		#self.template_loader = FileSystemLoader([TEMPLATE_ROOT, os.path.join(PLUGIN_ROOT, "%s/layout" % self.name)])
		#self.template_env = Environment(loader = self.template_loader)
		print("Initializing plugin: %s" % self.name)
