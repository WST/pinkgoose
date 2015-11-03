# -*- coding: utf-8 -*-

# Flask
from flask import Flask

# Python
import os

CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/default')

application = Flask(__name__, template_folder = TEMPLATE_ROOT)
application.config.from_object('config')

from cms import views
