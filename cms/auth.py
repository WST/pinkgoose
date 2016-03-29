# -*- coding: utf-8 -*-

# Flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g

# Наше приложение
from cms import application, login_manager
from cms.forms import LoginForm
from cms.classes import User

@application.before_request
def before_request():
	g.user = current_user

@application.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect('/')
	
	form = LoginForm()

	if form.validate_on_submit():
		user = User.authenticate(form.username.data, form.password.data)
		if user is not None:
			login_user(user)
			return redirect('/')
		else:
			return render_template('auth/login-page.htt', title = u'Авторизация', form = form)
	else:
		return render_template('auth/login-page.htt', title = u'Авторизация', form = form)

login_manager.login_view = 'login'

@application.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect('/')
