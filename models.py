import json

def cargar_productos():
    with open('data/productos.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def guardar_productos(productos):
    with open('data/productos.json', 'w', encoding='utf-8') as file:
        json.dump(productos, file, indent=4, ensure_ascii=False)

# def cargar_usuarios():
#     with open('data/usuarios.json', 'uc', encoding='utf-8') as file:
#         return json.load(file)

# def guardar_usuarios(usuarios):
#     with open('data/usuarios.json', 'ug', encoding='utf-8') as file:
#         json.dump(usuarios, file, indent=4, ensure_ascii=False)