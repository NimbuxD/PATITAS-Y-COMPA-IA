from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_restful import Api, Resource
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
api = Api(app)
app.secret_key = 'supersecretkey'

# Rutas de los archivos JSON
PRODUCTS_FILE = os.path.join(app.root_path, 'data', 'productos.json')
USERS_FILE = os.path.join(app.root_path, 'data', 'usuarios.json')

# Función para cargar productos desde un archivo JSON con codificación UTF-8
def cargar_productos():
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para cargar usuarios desde un archivo JSON con codificación UTF-8
def cargar_usuarios():
    if not os.path.exists(USERS_FILE):
        return []  # Retornar una lista vacía si el archivo no existe
    with open(USERS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para guardar usuarios en un archivo JSON con codificación UTF-8
def guardar_usuarios(usuarios):
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, ensure_ascii=False, indent=4)

# API Resource para productos
class ProductoListResource(Resource):
    def get(self):
        return cargar_productos()

class ProductoResource(Resource):
    def get(self, id):
        productos = cargar_productos()
        producto = next((item for item in productos if item['id'] == id), None)
        if producto:
            return producto
        return {'message': 'Producto no encontrado'}, 404

# API Resource para usuarios
class UsuarioResource(Resource):
    def post(self):
        usuarios = cargar_usuarios()
        nuevo_usuario = request.json
        email = nuevo_usuario.get('email')
        if any(usuario['email'] == email for usuario in usuarios):
            return {'message': 'El correo electrónico ya está en uso'}, 400
        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)
        return {'message': 'Usuario registrado con éxito'}, 201

class LoginResource(Resource):
    def post(self):
        datos = request.json
        email = datos.get('email')
        password = datos.get('password')
        usuarios = cargar_usuarios()
        usuario = next((u for u in usuarios if u['email'] == email and u['password'] == password), None)
        if usuario:
            session['usuario'] = usuario
            return {'message': 'Inicio de sesión exitoso'}, 200
        return {'message': 'Correo electrónico o contraseña incorrectos'}, 401

class ActualizarPerfilResource(Resource):
    def post(self):
        if 'usuario' not in session:
            return {'message': 'Usuario no autenticado'}, 401

        datos_actualizados = request.json
        email = session['usuario']['email']
        usuarios = cargar_usuarios()
        for usuario in usuarios:
            if usuario['email'] == email:
                usuario['telefono'] = datos_actualizados.get('telefono', usuario.get('telefono'))
                usuario['email'] = datos_actualizados.get('email', usuario.get('email'))
                usuario['direccion'] = datos_actualizados.get('direccion', usuario.get('direccion'))
                session['usuario'] = usuario
                guardar_usuarios(usuarios)
                return {'message': 'Perfil actualizado con éxito'}, 200

        return {'message': 'Usuario no encontrado'}, 404

# Rutas de la API
api.add_resource(ProductoListResource, '/api/productos')
api.add_resource(ProductoResource, '/api/productos/<int:id>')
api.add_resource(UsuarioResource, '/api/usuarios')
api.add_resource(LoginResource, '/api/login')
api.add_resource(ActualizarPerfilResource, '/api/actualizar_perfil')

# Ruta para cerrar sesión
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    return jsonify({'message': 'Sesión cerrada con éxito'}), 200

# Rutas para las páginas HTML
@app.route('/')
def index():
    return render_template('index.html', usuario=session.get('usuario'))

@app.route('/productos')
def productos():
    return render_template('productos.html', usuario=session.get('usuario'))

@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html', usuario=session['usuario'])

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', usuario=session.get('usuario'))

@app.route('/login')
def login():
    return render_template('login.html', usuario=session.get('usuario'))

@app.route('/producto/<int:product_id>')
def producto(product_id):
    productos = cargar_productos()
    producto = next((item for item in productos if item['id'] == product_id), None)
    if producto:
        # Calcular el precio con descuento
        descuento = producto['precio'] * 0.05
        precio_con_descuento = int(producto['precio'] - descuento)
        return render_template('producto.html', product=producto, precio_con_descuento=precio_con_descuento, usuario=session.get('usuario'))
    else:
        return "Producto no encontrado", 404

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    print(f"Datos recibidos: {data}")
    product_id = data['product_id']
    product_name = data['product_name']
    product_price = data['product_price']
    product_foto = data['product_foto']
    
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append({
        'product_id': product_id,
        'product_name': product_name,
        'product_price': product_price,
        'product_foto': product_foto
    })
    print(f"Carrito actualizado: {session['cart']}")  
    return jsonify({'message': 'Product added to cart', 'cart': session['cart']})

@app.route('/get_cart', methods=['GET'])
def get_cart():
    try:
        cart = session.get('cart', [])
        return jsonify(cart)
    except Exception as e:
        print(f"Error al obtener el carrito: {e}")
        return jsonify({'error': 'Ocurrió un error al obtener el carrito'}), 500

if __name__ == '__main__':
    app.run(debug=True)
