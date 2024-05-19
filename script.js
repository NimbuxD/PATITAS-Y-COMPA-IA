$(document).ready(function () {
    $('#loginForm').submit(function (event) {
        event.preventDefault(); // Prevenir el envío del formulario

        // Limpiar errores anteriores
        $('#emailError').text('');
        $('#passwordError').text('');

        // Obtener valores
        var email = $('#email').val();
        var password = $('#password').val();
        var isValid = true;

        // Validar correo electrónico
        if (!email) {
            $('#emailError').text('El correo electrónico es obligatorio.');
            isValid = false;
        } else if (!validateEmail(email)) {
            $('#emailError').text('Por favor, ingresa un correo electrónico válido.');
            isValid = false;
        }

        // Validar contraseña
        if (!password) {
            $('#passwordError').text('La contraseña es obligatoria.');
            isValid = false;
        } else if (password.length < 6) {
            $('#passwordError').text('La contraseña debe tener al menos 6 caracteres.');
            isValid = false;
        }

        // Si es válido, enviar el formulario
        if (isValid) {
            this.submit();
        }
    });

    function validateEmail(email) {
        var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return re.test(email);
    }
});