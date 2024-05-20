$(document).ready(function () {
    // validacion registro
    $('#registroForm').on('submit', function (event) {
        event.preventDefault();

        let isValid = true;

        // Validar nombre
        if ($('#nombre').val().trim() === '') {
            $('#nombreError').text('El nombre es obligatorio');
            isValid = false;
        } else {
            $('#nombreError').text('');
        }

        // Validar apellido
        if ($('#apellido').val().trim() === '') {
            $('#apellidoError').text('El apellido es obligatorio');
            isValid = false;
        } else {
            $('#apellidoError').text('');
        }

        // Validar teléfono
        const phonePattern = /^[0-9]+$/;
        if (!phonePattern.test($('#telefono').val().trim())) {
            $('#telefonoError').text('El teléfono debe contener solo números');
            isValid = false;
        } else {
            $('#telefonoError').text('');
        }

        // Validar correo electrónico
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test($('#email').val().trim())) {
            $('#emailError').text('El correo electrónico no es válido');
            isValid = false;
        } else {
            $('#emailError').text('');
        }

        // Validar dirección
        if ($('#direccion').val().trim() === '') {
            $('#direccionError').text('La dirección es obligatoria');
            isValid = false;
        } else {
            $('#direccionError').text('');
        }

        if (isValid) {
            this.submit();
        }
    });

    // validacion login
    $('#loginForm').on('submit', function(event) {
        event.preventDefault();
        
        let isValid = true;

        // Validar correo electrónico
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test($('#email').val().trim())) {
            $('#emailError').text('El correo electrónico no es válido');
            isValid = false;
        } else {
            $('#emailError').text('');
        }

        // Validar contraseña
        if ($('#password').val().trim() === '') {
            $('#passwordError').text('La contraseña es obligatoria');
            isValid = false;
        } else {
            $('#passwordError').text('');
        }

        if (isValid) {
            this.submit();
        }
    });

    // validacion contacto
    $('#contactoForm').on('submit', function (event) {
        event.preventDefault();
    
        let isValid = true;
    
        // Validar nombre
        if ($('#nombre').val().trim() === '') {
            $('#nombreError').text('El nombre es obligatorio');
            isValid = false;
        } else {
            $('#nombreError').text('');
        }
    
        // Validar teléfono
        const phonePattern = /^[0-9]+$/;
        if (!phonePattern.test($('#telefono').val().trim())) {
            $('#telefonoError').text('El teléfono debe contener solo números');
            isValid = false;
        } else {
            $('#telefonoError').text('');
        }
    
        // Validar correo electrónico
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test($('#email').val().trim())) {
            $('#emailError').text('El correo electrónico no es válido');
            isValid = false;
        } else {
            $('#emailError').text('');
        }
    
        if (isValid) {
            this.submit();
        }
    });

    // validacion compra
    $('.add-to-cart').on('click', function(event) {
        event.preventDefault();
        
        if (confirm('¿Estás seguro de que quieres agregar este producto al carrito?')) {
            // Lógica para agregar el producto al carrito
        }
    });
});

[
    {
        "id": 1,
        "name": "Bandana para Mascotas",
        "description": "Hermosas bandanas de diferentes tamaños y diseños.",
        "price": 5000,
        "image": "../../img/bandana.webp",
        "link": "../HTML/productos/bandana.html"
    },
    {
        "id": 2,
        "name": "Correa para Mascotas",
        "description": "Correas resistentes y cómodas para el paseo diario.",
        "price": 10000,
        "image": "../img/correa.webp",
        "link": "../HTML/productos/correa.html"
    },
    {
        "id": 3,
        "name": "identicación",
        "description": "Placas de identificación personalizables.",
        "price": 4.000,
        "image": "../img/identificacion.webp",
        "link": "../HTML/productos/identificacion.html"
    },
    {
        "id": 4,
        "name": "pelota",
        "description": "Pelota de caucho resistente a cualquier mascota.",
        "price": 10000,
        "image": "../img/pelota.webp",
        "link": "../HTML/productos/pelota.html"
    },
    {
        "id": 5,
        "name": "rascador",
        "description": "Rascador para gatos de madera y zonas acolchadas.",
        "price": 20000,
        "image": "../img/rascador.webp",
        "link": "../HTML/productos/rascador.html"
    }

]
