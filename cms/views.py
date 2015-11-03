# -*- coding: utf-8 -*-

# Наше приложение
from cms import application as app, db

# Flask
from flask import render_template
from flask.ext.login import login_required

@app.route('/')
def home_page():
	cur = db.connection.cursor()
	return render_template('home-page.htt', title = u'Главная страница')
