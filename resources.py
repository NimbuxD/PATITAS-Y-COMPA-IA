from flask_restful import Resource, reqparse
from models import cargar_productos, guardar_productos

# Productos
class ProductoResource(Resource):
    def get(self, id):
        productos = cargar_productos()
        producto = next((p for p in productos if p['id'] == id), None)
        if producto:
            return producto, 200
        return {'message': 'Producto no encontrado'}, 404

    def delete(self, id):
        productos = cargar_productos()
        productos = [p for p in productos if p['id'] != id]
        guardar_productos(productos)
        return '', 204

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre')
        parser.add_argument('precio', type=float)
        parser.add_argument('descripcion')
        parser.add_argument('foto')
        data = parser.parse_args()

        productos = cargar_productos()
        producto = next((p for p in productos if p['id'] == id), None)
        if producto:
            producto.update(data)
            guardar_productos(productos)
            return producto, 200
        return {'message': 'Producto no encontrado'}, 404

class ProductoListResource(Resource):
    def get(self):
        return cargar_productos(), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('precio', type=float, required=True)
        parser.add_argument('descripcion', required=True)
        parser.add_argument('foto', required=True)
        data = parser.parse_args()

        productos = cargar_productos()
        nuevo_producto = {
            'id': len(productos) + 1,
            'nombre': data['nombre'],
            'precio': data['precio'],
            'descripcion': data['descripcion'],
            'foto': data['foto']
        }
        productos.append(nuevo_producto)
        guardar_productos(productos)
        return nuevo_producto, 201

# Usuarios
# class UsuariosResource(Resource):
#     def get(self, id):
#         Usuarios = cargar_usuarios()
#         usuarios  = next((p for p in usuarios if p['id'] == id), None)
#         if usuarios :
#             return usuarios , 200
#         return {'message': 'usuarios  no encontrado'}, 404

#     def delete(self, id):
#         usuarios  = cargar_usuarios ()
#         usuarios  = [p for p in usuarios  if p['id'] != id]
#         guardar_usuarios (usuarios)
#         return '', 204

#     def put(self, id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('NombreCompleto')
#         parser.add_argument('telefono', type=float)
#         parser.add_argument('correo')
#         data = parser.parse_args()

#         usuarios = cargar_productos()
#         usuarios  = next((p for p in usuarios  if p['id'] == id), None)
#         if usuarios :
#            usuarios .update(data)
#             guardar_usuarios (usuarios )
#             return producto, 200
#         return {'message': 'Producto no encontrado'}, 404





# class UsuariosListResource(Resource):
#     def get(self):
#         return cargar_productos(), 200

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('nombre', required=True)
#         parser.add_argument('precio', type=float, required=True)
#         parser.add_argument('descripcion', required=True)
#         parser.add_argument('foto', required=True)
#         data = parser.parse_args()

#         productos = cargar_productos()
#         nuevo_producto = {
#             'id': len(productos) + 1,
#             'nombre': data['nombre'],
#             'precio': data['precio'],
#             'descripcion': data['descripcion'],
#             'foto': data['foto']
#         }
#         productos.append(nuevo_producto)
#         guardar_productos(productos)
#         return nuevo_producto, 201