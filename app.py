from controladores.controllerProducto import *
from flask import Flask
import pymongo

# Crear el objeto flask
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./static/imagenes"

# Crear la conexión a mongo
miConexion = pymongo.MongoClient("mongodb+srv://angel27:1234@cluster0.sisg7tu.mongodb.net/?retryWrites=true&w=majority")

# Acceder a la base de datos
baseDatos = miConexion["GESTIONPRODUCTOS"]

# Crear objeto para referenciar la colección
productos = baseDatos["PRODUCTOS"]



if __name__ == "__main__":
    app.run(port=3000, debug=True)

