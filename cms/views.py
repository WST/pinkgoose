# -*- coding: utf-8 -*-

# Наше приложение
from cms import application as app

# Flask
from flask import render_template

@app.route('/')
def home_page():
	user = {'nickname': 'Miguel'} # выдуманный пользователь
	return render_template("home-page.htt", title = u'Главная страница', user = user)
