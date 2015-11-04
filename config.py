# -*- coding: utf-8 -*-

# Flask
CSRF_ENABLED = True
SECRET_KEY = 'n2NXnies98enr9s'
DEBUG = True

# PostgreSQL
PG_HOST = 'localhost'
PG_USER = 'averkov'
PG_PASSWORD = ''
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
	'<div style="position: relative; top: -32px; left: 600px; width: 293px; height: 230px; background-image: url(\'/static/ponies/pinkie-1.png\');" id="pony"></div>',
	'<div style="position: relative; top: -32px; left: 700px; width: 208px; height: 230px; background-image: url(\'/static/ponies/twilight-1.png\');" id="pony"></div>',
]
