# -*- coding: utf-8 -*-

# Наше приложение
from cms import application, db, db_cursor
from cms.forms import *

# Flask
from flask import render_template, current_app, request, redirect
from flask.ext.login import login_required

# Python
import random

@application.route('/admin')
@login_required
def admin_main_page():
	return render_template('admin/main-page.htt', title = u'Администрирование')

@application.route('/admin/posts')
@login_required
def admin_posts_page():
	return render_template('admin/posts-page.htt', title = u'Посты блога')

@application.route('/admin/posts/add', methods = ['GET', 'POST'])
@login_required
def admin_post_add_page():
	form = PostForm()
	if form.validate_on_submit():
		pass

	return render_template('admin/post-add-page.htt', title = u'Добавление записи', form = form)
