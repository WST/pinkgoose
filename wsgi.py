import bottle
from bottle import route, run, template

@route('/')
def index():
    return template('<b>Hello {{name}}</b>!', name = 'foo')

if __name__ == '__main__':
	run(host = 'localhost', port = 8080)
else:
	application = bottle.default_app()
