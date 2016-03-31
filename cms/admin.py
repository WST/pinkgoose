# -*- coding: utf-8 -*-

# Наше приложение
from cms import application, db
from cms.forms import *

# Flask
from flask import render_template, current_app, request, redirect
from flask.ext.login import login_required

# Python
import random
import time

@application.route('/admin')
@login_required
def admin_main_page():
	return render_template('admin/main-page.htt', title = u'Администрирование')

@application.route('/admin/posts')
@login_required
def admin_posts_page():
	cur = db.cursor()
	cur.execute("SELECT * FROM posts ORDER BY published_at DESC")
	posts = cur.fetchall()
	return render_template('admin/posts-page.htt', title = u'Посты блога', posts = posts)

@application.route('/admin/posts/add', methods = ['GET', 'POST'])
@login_required
def admin_post_add_page():
	form = PostForm()
	if form.validate_on_submit():
		title = form.data['title']
		slug = form.data['slug']
		intro = form.data['intro']
		fulltext = form.data['fulltext']

		data = (title, slug, intro, fulltext, 1)
		
		try:
			cur = db.cursor()
			cur.execute("INSERT INTO posts (title, slug, intro, fulltext, published, published_at, author_id) VALUES (%s, %s, %s, %s, TRUE, EXTRACT(EPOCH FROM NOW()), %s)", data);
			db.commit()
		except:
			db.rollback()

		# Перенаправление
		return redirect('/admin/posts')

	return render_template('admin/post-add-page.htt', title = u'Добавление записи', form = form)
