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

class Site:
	def __init__(self):
		self.application = Flask(__name__, template_folder = TEMPLATE_ROOT, static_folder = STATIC_ROOT)
		self.application.config.from_object('config')
		self.db = PostgreSQL(self.application)
		self.initialize_login_manager()

		with self.application.app_context():
			self.initialize_modules()

	def initialize_login_manager(self):
		self.login_manager = LoginManager()
		self.login_manager.init_app(self.application)

	def initialize_module(self, module_row):
		try:
			module = importlib.import_module('module', module_row['name'])
			module.start(self)
		except Exception as e:
			print(str(e))

	def initialize_modules(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM modules WHERE enabled = TRUE")
		modules = cursor.fetchall()
		map(self.initialize_module, modules)
		db.close()
