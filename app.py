from flask import Flask, render_template, jsonify
from flask_restful import Api
from resources import ProductoResource, ProductoListResource
import json  # Asegúrate de importar json

app = Flask(__name__, static_folder='static', template_folder='templates')
api = Api(app)

# Función para cargar productos desde un archivo JSON con codificación UTF-8
def cargar_productos():
    with open('data/productos.json', 'r', encoding='utf-8') as file:
        return json.load(file)
# def cargar_usuarios():
#     with open('data/usuarios.json', 'uc', encoding='utf-8') as file:
#         return json.load(file)

# Rutas de la API
api.add_resource(ProductoListResource, '/api/productos')
api.add_resource(ProductoResource, '/api/productos/<int:id>')
# api.add_resource(ProductoListResource, '/api/usuarios')
# api.add_resource(ProductoResource, '/api/usuarios/<int:id>')

# Rutas para las páginas HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/producto')
def producto():
    return render_template('producto.html')

if __name__ == '__main__':
    app.run(debug=True)
