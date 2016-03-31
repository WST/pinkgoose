# -*- coding: utf-8 -*-

# Наше приложение
from cms import application, db

# Flask
from flask import render_template, current_app
from flask.ext.login import login_required

# Python
import random

@application.route('/')
def home_page():
	cur = db.cursor()
	cur.execute("SELECT * FROM posts ORDER BY published_at DESC")
	posts = cur.fetchall()
	return render_template('home-page.htt', title = u'Главная страница', posts = posts)
