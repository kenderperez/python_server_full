from flask import Flask, request
from flask_pymongo import PyMongo
from flask_pymongo import pymongo
from bson import json_util
from flask import jsonify
from flask import render_template, send_from_directory
import os
ruta = os.getcwd()
app = Flask(__name__)
#mongo dbatlasconection
connection_string = 'mongodb+srv://root:fkFx2e73AkiR3dWU@cluster0-prrjn.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(connection_string)
db = client.get_database('dolar') # aca va el nombre de la base de datos donde dice 'dolar'
user_collection = pymongo.collection.Collection(db, 'user_collection')
#app.config['MONGO_URI']='mongodb://localhost/users'
#mongo = PyMongo(app)

#RUTAS
"""@app.route('/users', methods=['POST'])
def create_user():
	#Reciviendo datos
	nombre = request.json['nombre']
	edad = request.json['edad']
	if nombre and edad:
		mongo.db.users.insert({
			'nombre': nombre,
			'edad': edad
			})
		response = jsonify({'mensaje': 'usuario agregado'})
	else:
		response = jsonify({'mensaje': 'faltan datos'})


	return response

"""

@app.route('/', methods=['GET'])
def rutaInicial():
	#users = mongo.db.users.find()
	#response = json_util.dumps(users)
	#jonres = jsonify(response)
	return render_template('index.html')


@app.route('/', methods=['POST'])
def create_user():
	#REciviendo datos
	print(request.json)
	texto = request.json['texto']
	print(texto)
	print(type(texto))
	db.historicoToday.insert({ 'texto' : texto })
 
	#enviamos respuesta de que recibimos los datos del formulario
	response = jsonify({'mensaje':'datos recividos'})
	return response

#enviar archivos estaticos aca se estan enviando las carpetas css y js que estan dentro de src
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

"""

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
	
	users = mongo.db.users.find_one({'nombre': id})
	response = json_util.dumps(users)
	return response

@app.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
	
	users = mongo.db.users.delete_one({'nombre': id})
	response = jsonify({'mensaje':'usuario eliminado'})
	return response

"""




#EJECUCION DEL SEVIDOR
if __name__ == '__main__':
	app.run(debug=True, port=3000)
