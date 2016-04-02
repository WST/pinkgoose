# -*- coding: utf-8 -*-

# Наше приложение
from cms import site
from cms.forms import *

# Flask
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required

# Python
import random
import time

@site.application.route('/admin')
@login_required
def admin_main_page():
	return render_template('admin/main-page.htt', title = u'Администрирование')

@site.application.route('/admin/posts')
@login_required
def admin_posts_page():
	cursor = site.db.cursor()
	cursor.execute("SELECT * FROM posts ORDER BY published_at DESC")
	posts = cursor.fetchall()
	return render_template('admin/posts-page.htt', title = u'Посты блога', posts = posts)

@site.application.route('/admin/posts/add', methods = ['GET', 'POST'])
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
			cursor = site.db.cursor()
			cursor.execute("INSERT INTO posts (title, slug, intro, fulltext, published, published_at, author_id) VALUES (%s, %s, %s, %s, TRUE, EXTRACT(EPOCH FROM NOW()), %s)", data);
			db.commit()
		except:
			db.rollback()

		# Перенаправление
		return redirect(url_for('admin_posts_page'))

	return render_template('admin/post-add-page.htt', title = u'Добавление записи', form = form)
