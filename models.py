import json

def cargar_productos():
    with open('data/productos.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def guardar_productos(productos):
    with open('data/productos.json', 'w', encoding='utf-8') as file:
        json.dump(productos, file, indent=4, ensure_ascii=False)
