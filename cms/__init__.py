# -*- coding: utf-8 -*-

# Flask
from flask import Flask
#from flask.ext.mysqldb import MySQL
from flask.ext.postgresdb import PostgreSQL

# Python
import os

CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/default')

application = Flask(__name__, template_folder = TEMPLATE_ROOT)
application.config.from_object('config')

db = PostgreSQL(application)

from cms import views
