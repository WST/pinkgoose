# -*- coding: utf-8 -*-

# psycopg2
import psycopg2
import psycopg2.extras

# Flask
from flask import _app_ctx_stack, current_app

# NOTE: http://flask.pocoo.org/docs/0.10/extensiondev/

class PostgreSQL(object):
	def __init__(self, app = None):
		self.app = app
		if app is not None:
			self.init_app(app)

	def init_app(self, app):
		app.config.setdefault('PG_HOST', 'localhost')
		app.config.setdefault('PG_USER', None)
		app.config.setdefault('PG_PASSWORD', None)
		app.config.setdefault('PG_DB', None)

		if hasattr(app, 'teardown_appcontext'):
			app.teardown_appcontext(self.teardown)

	@property
	def connect(self):
		kwargs = {}

		for i in ['HOST', 'DATABASE', 'USER', 'PASSWORD']:
			config_name = "PG_%s" % i
			if current_app.config[config_name]:
				kwargs[i.lower()] = current_app.config[config_name]

		return psycopg2.connect(**kwargs)

	def standalone_connection(self):
		from config import PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD
		return psycopg2.connect(host = PG_HOST, database = PG_DATABASE, user = PG_USER, password = PG_PASSWORD)

	@property
	def connection(self):
		ctx = _app_ctx_stack.top
		if ctx is not None:
			if not hasattr(ctx, 'pg_db'):
				ctx.pg_db = self.connect
			return ctx.pg_db

	def teardown(self, exception):
		ctx = _app_ctx_stack.top
		if hasattr(ctx, 'pg_db'):
			ctx.pg_db.close()

	def commit(self):
		return self.connection.commit()

	def rollback(self):
		return self.connection.rollback()

	def cursor(self):
		return self.connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
