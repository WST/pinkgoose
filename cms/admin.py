# -*- coding: utf-8 -*-

# Наше приложение
from cms import application, db, db_cursor
from cms.forms import *

# Flask
from flask import render_template, current_app
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
	form = PostForm()
	return render_template('admin/posts-page.htt', title = u'Посты блога', form = form)
