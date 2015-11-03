# -*- coding: utf-8 -*-

from cms import login_manager

class User(object):
	def __init__(self):
		pass

	is_authenticated = True

	@staticmethod
	def authenticate(username, password):
		print("AUTH %s, %s" % (username, password))
		#user = User()
		#return user
		return None

	@staticmethod
	def get(user_id):
		user = User()
		return user

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)
