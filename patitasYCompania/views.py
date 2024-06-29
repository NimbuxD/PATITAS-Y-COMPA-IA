from decimal import Decimal, ROUND_HALF_UP
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .models import Producto, Profile, CartItem
from .forms import ContactForm, LoginForm, ProductoForm, RegistroUsuarioForm
import json

# Vistas de la Página Principal
def index(request):
    productos_populares = Producto.objects.all()[:3]
    return render(request, 'patitasYCompania/index.html', {'productos_populares': productos_populares})

def success(request):
    return render(request, 'patitasYCompania/success.html')

# Vistas de Autenticación
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            cliente_group, created = Group.objects.get_or_create(name='Cliente')
            user.groups.add(cliente_group)
            
            send_mail(
                'Registro Exitoso en Patitas y Compañía',
                f'Bienvenido {user.username}, tiene un 30% de descuento en la primera compra de la tienda.',
                'patitasycompania@gmail.com',
                [user.email],
                fail_silently=False,
            )
            
            auth_login(request, user)
            messages.success(request, "Registro exitoso. Bienvenido a Patitas y Compañía.")
            return redirect('user_profile')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'patitasYCompania/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, 'patitasYCompania/login.html', {'form': form, 'error': 'Credenciales incorrectas'})
    else:
        form = LoginForm()
    return render(request, 'patitasYCompania/login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('nombre')
        user.profile.telefono = request.POST.get('telefono')
        user.profile.direccion = request.POST.get('direccion')
        user.save()
        user.profile.save()
        messages.success(request, 'Perfil actualizado correctamente.')
    return render(request, 'patitasYCompania/perfil.html', {'usuario': user})

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
        return redirect('index')

# Vistas de Producto
def product_list(request):
    products = Producto.objects.all()
    return render(request, 'patitasYCompania/productos.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    return render(request, 'patitasYCompania/producto.html', {'product': product})

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

# Vistas de Contacto
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            enviar_correo_contacto(form.cleaned_data)
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'patitasYCompania/contacto.html', {'form': form})

# Vistas de Carrito de Compras
@login_required
def add_to_cart(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'¡{producto.nombre} ha sido añadido al carrito!')
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.producto.precio * item.quantity for item in cart_items)
    iva = total * Decimal(0.19)
    total_iva = total + iva

    if not request.user.profile.has_purchased:
        descuento = total_iva * Decimal(0.30)
        total_con_descuento = total_iva - descuento
    else:
        descuento = Decimal(0)
        total_con_descuento = total_iva

    total_iva = total_iva.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    iva = iva.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    total_con_descuento = total_con_descuento.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    descuento = descuento.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    return render(request, 'patitasYCompania/cart.html', {
        'cart_items': cart_items,
        'total': total_iva,
        'iva': iva,
        'descuento': descuento,
        'total_con_descuento': total_con_descuento,
    })

@login_required
def update_cart(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return JsonResponse({'message': 'Carrito actualizado correctamente'})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'El producto ha sido eliminado del carrito.')
    return redirect('cart')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, 'El carrito ha sido vaciado.')
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        name_on_card = request.POST.get('name_on_card')
        
        # Aquí puedes agregar la lógica para procesar el pago
        # como conectarte a un gateway de pago
        
        # Simulación de un pago exitoso
        messages.success(request, "Pago realizado con éxito.")
        request.user.profile.has_purchased = True
        request.user.profile.save()

        # Enviar correo con el detalle de la compra
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.producto.precio * item.quantity for item in cart_items)
        product_details = "\n".join([f"{item.quantity} x {item.producto.nombre} - ${item.producto.precio}" for item in cart_items])

        send_mail(
            'Gracias por tu compra en Patitas y Compañía',
            f'Hola {request.user.username},\n\nGracias por tu compra. Aquí tienes el detalle de los productos:\n\n{product_details}\n\nTotal: ${total}\n\n¡Esperamos verte pronto!',
            'patitasycompania@gmail.com',
            [request.user.email],
            fail_silently=False,
        )

        # Vaciar el carrito después del pago
        cart_items.delete()

        return redirect('success')
    
    return render(request, 'patitasYCompania/checkout.html')


# Vistas de Prueba de Envío de Correo
def test_email(request):
    try:
        send_mail(
            'Prueba de Envío de Correo',
            'Este es un correo de prueba.',
            'patitasycompania@gmail.com',
            ['destinatario@example.com'],
            fail_silently=False,
        )
        return HttpResponse("Correo enviado correctamente")
    except Exception as e:
        return HttpResponse(f"Error al enviar el correo: {e}")

# Funciones Auxiliares
def enviar_correo_contacto(data):
    try:
        send_mail(
            'Nuevo mensaje de contacto',
            f'Nombre: {data.get("nombre")}\nTeléfono: {data.get("telefono")}\nCorreo electrónico: {data.get("email")}\nMensaje:\n{data.get("mensaje")}',
            'patitasycompania@gmail.com',
            ['illanesluis18@gmail.com'],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
