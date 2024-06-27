from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm
import json

def index(request):
    return render(request, 'patitasYCompania/index.html')

def product_list(request):
    products = Producto.objects.all()
    return render(request, 'patitasYCompania/productos.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    return render(request, 'patitasYCompania/producto.html', {'product': product})

def contact(request):
    return render(request, 'patitasYCompania/contacto.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return render(request, 'patitasYCompania/login.html', {'error': 'Correo electrónico o contraseña incorrectos'})
    return render(request, 'patitasYCompania/login.html')

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'patitasYCompania/perfil.html', {'usuario': user})

@login_required
def user_logout(request):
    auth_logout(request)
    return JsonResponse({'message': 'Sesión cerrada con éxito'})

@login_required
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product_name = data['product_name']
    product_price = data['product_price']
    product_foto = data['product_foto']
    
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    request.session['cart'].append({
        'product_id': product_id,
        'product_name': product_name,
        'product_price': product_price,
        'product_foto': product_foto
    })
    request.session.modified = True
    return JsonResponse({'message': 'Producto añadido al carrito', 'cart': request.session['cart']})

def get_cart(request):
    try:
        cart = request.session.get('cart', [])
        return JsonResponse(cart, safe=False)
    except Exception as e:
        print(f"Error al obtener el carrito: {e}")
        return JsonResponse({'error': 'Ocurrió un error al obtener el carrito'}, status=500)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductoForm()
    return render(request, 'patitasYCompania/product_form.html', {'form': form})

@login_required
def product_update(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductoForm(instance=product)
    return render(request, 'patitasYCompania/product_form.html', {'form': form})

@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'patitasYCompania/product_confirm_delete.html', {'product': product})
