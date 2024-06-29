from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Usuario
from .forms import ContactForm, LoginForm, ProductoForm, RegistroUsuarioForm
import json

# Vistas de la Página Principal
def index(request):
    productos_populares = Producto.objects.all()[:3]  # Llama a los 3 primeros productos
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
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                try:
                    enviar_correo_bienvenida(user)
                except Exception as e:
                    print(f"Error al enviar el correo de bienvenida: {e}")
                return redirect('index')
            else:
                return render(request, 'patitasYCompania/registro.html', {'form': form, 'error': 'No se pudo autenticar al usuario. Por favor, intente nuevamente.'})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'patitasYCompania/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, 'patitasYCompania/login.html', {'form': form, 'error': 'Correo electrónico o contraseña incorrectos'})
    else:
        form = LoginForm()
    return render(request, 'patitasYCompania/login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def user_profile(request):
    return render(request, 'patitasYCompania/perfil.html', {'usuario': request.user})

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
            return redirect('success')  # Redirige a una página de éxito después de enviar el formulario
    else:
        form = ContactForm()
    return render(request, 'patitasYCompania/contacto.html', {'form': form})

# Vistas de Carrito de Compras
@login_required
def add_to_cart(request):
    data = json.loads(request.body)
    cart = request.session.get('cart', [])

    cart.append({
        'product_id': data['product_id'],
        'product_name': data['product_name'],
        'product_price': data['product_price'],
        'product_foto': data['product_foto']
    })
    
    request.session['cart'] = cart
    request.session.modified = True
    return JsonResponse({'message': 'Producto añadido al carrito', 'cart': cart})

def get_cart(request):
    try:
        cart = request.session.get('cart', [])
        return JsonResponse(cart, safe=False)
    except Exception as e:
        print(f"Error al obtener el carrito: {e}")
        return JsonResponse({'error': 'Ocurrió un error al obtener el carrito'}, status=500)

# Vistas de Prueba de Envío de Correo
def test_email(request):
    try:
        send_mail(
            'Prueba de Envío de Correo',
            'Este es un correo de prueba.',
            'patitasycompania@gmail.com',  # Correo del remitente
            ['destinatario@example.com'],  # Reemplaza esto con el correo de destino
            fail_silently=False,
        )
        return HttpResponse("Correo enviado correctamente")
    except Exception as e:
        return HttpResponse(f"Error al enviar el correo: {e}")

# Funciones Auxiliares
def enviar_correo_bienvenida(user):
    try:
        email_subject = 'Bienvenido a Patitas y Compañía'
        email_body = f"""
        Hola {user.username},

        Gracias por registrarte en nuestra página. Como agradecimiento, te ofrecemos un descuento del 30% en tu primera compra.

        ¡Disfruta de tu experiencia en Patitas y Compañía!
        """
        print("Enviando correo a:", user.email)
        send_mail(
            email_subject,
            email_body,
            'patitasycompania@gmail.com',
            [user.email],
            fail_silently=False,
        )
        print("Correo enviado correctamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise e


def enviar_correo_contacto(data):
    try:
        send_mail(
            'Nuevo mensaje de contacto',
            f'Nombre: {data.get("nombre")}\nTeléfono: {data.get("telefono")}\nCorreo electrónico: {data.get("email")}\nMensaje:\n{data.get("mensaje")}',
            'patitasycompania@gmail.com',  # Correo del remitente
            ['illanesluis18@gmail.com'],  # Correo del destinatario
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
