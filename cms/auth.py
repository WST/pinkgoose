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
	g.user = current_user


@application.route('/login', methods = ['GET', 'POST'])
def login():
	print(current_user)
	if current_user is not None and current_user[0]:
		return redirect('/')
	
	form = LoginForm()

	if form.validate_on_submit():
		user = User.authenticate(form.username.data, form.password.data)
		if user is not None:
			login_user(user)
			flask.flash(u'Авторизация успешна')
			return redirect('/')
		else:
			return render_template('auth/login-page.htt', title = u'Авторизация', form = form)
	else:
		return render_template('auth/login-page.htt', title = u'Авторизация', form = form)

login_manager.login_view = 'login'
