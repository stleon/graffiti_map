from bottle import Bottle
from bottle import run
from bottle import template
from bottle import static_file
from bottle import install
from bottle import response
from bottle import request
from gdb import *
from pony.orm.integration.bottle_plugin import PonyPlugin

app = Bottle()

app.install(PonyPlugin())

#app.config['sqlite.db'] = ':memory:' # Tells the sqlite plugin which db to use
app.config['admin'] = 'leonst998@gmail.com'
app.config['domen'] = 'http://grafitty.net'

def send_to_admin(func):
	def wrapper(error):
		return func(error), ' Пришлите администратору (%s) следующее сообщение %s' % (app.config['admin'], error)
	return wrapper

def check_allowed_host(func):
	'''проверяем host-header'''
	def wrapper():
		#X-Forwarded-Host
		host = request.get_header('host')
		print(host)
		return func()
	return wrapper

@app.error(404)
@send_to_admin
def error404(error):
	return 'А тут ничего нет.'

@app.error(403)
@send_to_admin
def error403(error):
	return 'Недостаточно прав.'

"""
@app.error(500)
@send_to_admin
def error500(error):
	return 'Ошибка сервера.'
"""

@app.route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static')

@app.route('/dynamic/<filepath:path>')
def server_dynamic(filepath):
	return static_file(filepath, root='./dynamic')

@app.route('/robots.txt')
def robots():
	response.status = 200
	response.content_type = 'text/plain;'
	return 'User-agent: *\nDisallow: /admin\nHost: %s' % app.config['domen']

'''
@app.route('/sitemap.xml')
def sitemap():
	pass
'''

@app.route('/')
#@check_allowed_host
@app.route('/')
def index():
	gs = select(g for g in Graffity).order_by(Graffity.date_created)
	return template('main', gs=gs)

@app.route('/map-data')
def data_for_yandex_map():
	gs = select(g for g in Graffity)
	gs_json = { "type": "FeatureCollection", "features": []}
	i = 0
	for g in gs:
		baloon_help = 'Граффити «{name}»'.format(name=g.name)
		baloon_content = '''
		<img class="img-responsive" src="/dynamic/{image}" >

		'''.format(image=g.image)
		ballon_footer = '<a href="/graffities/{g}" target=_blank>Посмотреть и обсудить'.format(g=g.id)
		cluster_caption = 'Граффити {}'.format(g.id)
		gs_json["features"].append(
			{"type": "Feature", "id": i, "geometry": {"type": "Point", "coordinates": [g.lat, g.lon]}, 
			"properties": {"balloonContentHeader": baloon_help, "balloonContent": baloon_content, 
			"balloonContentFooter": ballon_footer,
			"clusterCaption": cluster_caption, "hintContent": baloon_help}},
			)
		i = i + 1

	return gs_json



@app.route('/graffities/<graffity_id:int>')
def graffity_page(graffity_id):
	g = Graffity[graffity_id]
	return template('graffity', g=g)

run(app, host='localhost', port=8000, debug=True, reloader=True)