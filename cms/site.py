# -*- coding: utf-8 -*-

# Flask
from flask import Flask
from flask.ext.postgresdb import PostgreSQL
from flask.ext.login import LoginManager

# Python
import os, sys, importlib

# config
from config import LAYOUT

# Некоторые пути
CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/' + LAYOUT)
STATIC_ROOT = os.path.join(CMS_ROOT, 'static')
PLUGIN_ROOT = os.path.join(CMS_ROOT, 'plugins')

importlib.invalidate_caches()
sys.path.append(PLUGIN_ROOT)

class Site:
	plugins = {}
	structure = []

	def __init__(self):
		self.application = Flask(__name__, template_folder = TEMPLATE_ROOT, static_folder = STATIC_ROOT)
		self.application.config.from_object('config')
		self.db = PostgreSQL(self.application)
		self.initialize_login_manager()

		with self.application.app_context():
			self.initialize_plugins()
			self.load_menu()
			self.setup_urls()

	def load_menu(self):
		self.structure = []
		cursor = self.db.cursor()
		cursor.execute("SELECT i.id AS id, i.parent AS parent, i.url AS url, i.title AS title, i.tooltip AS tooltip, p.name AS plugin FROM menu_items AS i JOIN plugins AS p ON i.plugin = p.id WHERE i.enabled = TRUE and p.enabled = TRUE")
		menu_items = cursor.fetchall()
		self.process_structure(menu_items)

	def process_structure(self, structure):
		for row in structure:
			self.structure += [row]

	def initialize_login_manager(self):
		self.login_manager = LoginManager()
		self.login_manager.init_app(self.application)

	def initialize_plugin(self, plugin_row):
		try:
			module = importlib.import_module('%s.plugin' % plugin_row['name'])
			plugin = module.CirnoPlugin(self)
			self.plugins[plugin_row['name']] = plugin
		except Exception as e:
			print(str(e))

	def initialize_plugins(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM plugins WHERE enabled = TRUE")
		plugins = cursor.fetchall()
		for plugin in plugins:
			self.initialize_plugin(plugin)

	def pattern_name(self, url_pattern):
		return url_pattern

	def setup_urls(self):
		for item in self.structure:
			try:
				self.application.add_url_rule(item['url'], self.pattern_name(item['url']), self.plugins[item['plugin']].handle_request)
			except Exception as e:
				print(str(e))
