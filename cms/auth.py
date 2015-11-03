# -*- coding: utf-8 -*-

# Flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g

# Наше приложение
from cms import application, login_manager
from forms import LoginForm
from classes import User

@application.before_request
def before_request():
	print("before_request called")
	g.user = current_user


@application.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect('/')
	
	form = LoginForm()

	if form.validate_on_submit():
		user = User.authenticate(form.username.data, form.password.data)
		if user is not None:
			g.user = user
		return redirect('/')
	else:
		return render_template('auth/login-page.htt', title = u'Авторизация', form = form)

login_manager.login_view = 'login'