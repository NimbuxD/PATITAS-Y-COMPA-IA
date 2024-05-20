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



$(document).ready(function () {
});

$(document).ready(function () {
});
