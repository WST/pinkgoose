# -*- coding: utf-8 -*-

# Python
import os

# Cirno
from cms import site
from cms.site import TEMPLATE_ROOT, PLUGIN_ROOT

from flask import Blueprint

class AbstractCirnoPlugin(Blueprint):
	template_loader = None
	template_env = None

	def __init__(self, site):
		self.site = site
		self.name = type(self).__module__.split('.')[0]
		print("Initializing plugin: %s" % self.name)
		static_folder = os.path.join(PLUGIN_ROOT, self.name, 'static')
		super(AbstractCirnoPlugin, self).__init__(self.name, __name__, static_url_path = '/static/%s' % self.name, static_folder = static_folder)
		site.application.register_blueprint(self)
