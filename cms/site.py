# -*- coding: utf-8 -*-

# Flask
from flask import Flask
from flask.ext.postgresdb import PostgreSQL
from flask.ext.login import LoginManager

# Python
import os
import sys

# psycopg2
import psycopg2
import psycopg2.extras

# config
from config import LAYOUT

# Некоторые пути
CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/' + LAYOUT)
STATIC_ROOT = os.path.join(CMS_ROOT, 'static')

class Site:
	db = None
	application = None

	def __init__(self):
		self.application = Flask(__name__, template_folder = TEMPLATE_ROOT, static_folder = STATIC_ROOT)
		self.application.config.from_object('config')

		self.connect_db()
		self.initialize_login_manager()

	def connect_db(self):
		self.db = PostgreSQL(self.application)

	def initialize_login_manager(self):
		self.login_manager = LoginManager()
		self.login_manager.init_app(self.application)
