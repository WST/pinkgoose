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

# Костыль, исправляющий проблему, когда Jinja2 не воспринимает данные как utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Некоторые пути
CMS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(CMS_ROOT, 'layout/default')

# Создаём приложение и загружаем конфиг
application = Flask(__name__, template_folder = TEMPLATE_ROOT)
application.config.from_object('config')

# Подключение к СУБД PostgreSQL
db = PostgreSQL(application)

def db_cursor():
	return db.connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

# Менеджер авторизаций
login_manager = LoginManager()
login_manager.init_app(application)

# Импортируем класс пользователя и другие
from cms import classes

# Импортируем наши виды
from cms import views

# Всё, что связано с авторизацией
from cms import auth
