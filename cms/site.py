# -*- coding: utf-8 -*-

# Flask
from flask import Flask, request, render_template
from flask.ext.postgresdb import PostgreSQL
from flask.ext.login import LoginManager

# Jinja2
import jinja2

# Python
import os, sys, importlib

# Werkzeug
from werkzeug.exceptions import abort

# config
from config import LAYOUT

# Некоторые пути
CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/' + LAYOUT)
STATIC_ROOT = os.path.join(TEMPLATE_ROOT, 'static')
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
			self.setup_template_loader()
			self.load_menu()
			self.setup_urls()

	def setup_template_loader(self):
		# http://reliablybroken.com/b/2012/05/custom-template-folders-with-flask/
		dirs = [os.path.join(PLUGIN_ROOT, i, 'templates') for i in self.plugins.keys()]
		loader = jinja2.ChoiceLoader([self.application.jinja_loader, jinja2.FileSystemLoader(dirs)])
		self.application.jinja_loader = loader

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

	def menu_item_by_path(self, path):
		for item in self.structure:
			if item['url'] == path:
				return item
		return None

	def handle_menu_item(self, error):
		item = self.menu_item_by_path(request.path)
		if item is None:
			return render_template('404-page.htt'), 404
		else:
			return self.plugins[item['plugin']].menu_item(request, item)

	def setup_urls(self):
		self.application.error_handler_spec[None][404] = self.handle_menu_item
