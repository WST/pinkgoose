# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

# Flask
CSRF_ENABLED = True
SECRET_KEY = 'n2NXnies98enr9s'
DEBUG = True

# PostgreSQL
PG_HOST = 'localhost'
PG_USER = 'averkov'
PG_PASSWORD = '123456'
PG_DATABASE = 'sometesting'

# Основные настройки сайта
LAYOUT = u'default'
SITE_TITLE = u'averkov.web.id'
SITE_SLOGAN = u'Жизнь, веб, XMPP, TAS, электронные самоделки'

# Сообщения, отображаемые в подвале сайта
FOOTER_MESSAGES = [
	u'Прощай, WordPress, я не буду скучать',
	u'Сайт работает не на WordPress',
	u'Сайт работает на не WordPress',
	u'WordPress — тормоз',
	u'Powered by Python, Flask, PostgreSQL, uWSGI & nginx',
	u'uWSGI — произведение искусства',
	u'uWSGI — серебряная пуля',
	u'Будь поняшей, не пользуйся WordPress',
]

# Поняшки :3
PONIES = [
	'<div style="position: relative; top: -7px; left: 700px; width: 200px; height: 233px; background-image: url(\'/static/ponies/applebloom-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: -2px; left: 800px; width: 164px; height: 200px; background-image: url(\'/static/ponies/applebloom-2.png\');" id="pony"></div>',
	'<div style="position: relative; top: -32px; left: 660px; width: 293px; height: 230px; background-image: url(\'/static/ponies/pinkie-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: -32px; left: 700px; width: 208px; height: 230px; background-image: url(\'/static/ponies/twilight-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: -11px; left: 600px; width: 174px; height: 242px; background-image: url(\'/static/ponies/dashie-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: -42px; left: 750px; width: 155px; height: 240px; background-image: url(\'/static/ponies/button-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: 0px; left: 750px; width: 159px; height: 198px; background-image: url(\'/static/ponies/button-2.png\');" id="pony"></div>',
	'<div style="position: relative; top: -42px; left: 750px; width: 173px; height: 240px; background-image: url(\'/static/ponies/button-3.png\');" id="pony"></div>',
]
