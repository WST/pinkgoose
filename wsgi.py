#!/usr/bin/env python
# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

import sys

from cms import site

using_uwsgi = False
try:
	import uwsgi
	using_uwsgi = True
	try:
		import uwsgidecorators
	except:
		print("Running under uWSGI, but also need uwsgidecorators module. Exitting.")
		sys.exit(-1)
except:
	print("Note: this application is meant to be run under uWSGI")

if using_uwsgi:
	print("Using uWSGI, perfect!")

if __name__ == "__main__":
	site.application.run()
