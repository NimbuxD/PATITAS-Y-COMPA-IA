$(document).ready(function () {
    // Captura el evento de envío del formulario
    $('#registroForm').submit(function (event) {
        // Evita que el formulario se envíe automáticamente
        event.preventDefault();

        // Obtiene los valores de los campos del formulario
        var nombre = $('#nombre').val().trim();
        var telefono = $('#telefono').val().trim();
        var email = $('#email').val().trim();
        var address = $('#address').val().trim();


        // Realiza las validaciones
     
        if (telefono === '') {
            alert('Por favor, ingresa tu número de teléfono.');
            return;
        }

        // Valida el formato del número de teléfono
        var telefonoRegex = /^[+]?\d{8,}$/;
        if (!telefonoRegex.test(telefono)) {
            alert('Por favor, ingresa un número de teléfono válido.');
            return;
        }

        if (email === '') {
            alert('Por favor, ingresa tu correo electrónico.');
            return;
        }

        // Valida el formato del correo electrónico
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, ingresa un correo electrónico válido.');
            return;
        }

        if (address === '') {
            alert('Por favor, ingresa tu dirección.');
            return;
        }

        // Muestra un mensaje de éxito
        alert('Los datos se han guardado exitosamente.');

        // Si todas las validaciones pasan, permite que el formulario se envíe
        this.submit();
    });
});
