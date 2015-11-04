# -*- coding: utf-8 -*-

# Наше приложение
from cms import application as app, db, db_cursor

# Flask
from flask import render_template
from flask.ext.login import login_required

@app.route('/')
def home_page():
	cur = db_cursor()
	cur.execute("SELECT * FROM posts ORDER BY published_at DESC")
	posts = cur.fetchall()
	return render_template('home-page.htt', title = u'Главная страница', posts = posts)
