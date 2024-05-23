$(document).ready(function () {
    $('#loginForm').on('submit', function (e) {
        e.preventDefault();
        let valid = true;

        // Validar correo electrónico
        const email = $('#email').val();
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(email)) {
            $('#emailError').text('Por favor, ingrese un correo electrónico válido.');
            valid = false;
        } else {
            $('#emailError').text('');
        }

        // Validar contraseña
        const password = $('#password').val();
        if (password.length < 6) {
            $('#passwordError').text('La contraseña debe tener al menos 6 caracteres.');
            valid = false;
        } else {
            $('#passwordError').text('');
        }

        if (valid) {
            // Enviar los datos de inicio de sesión a la API
            const loginData = {
                email: email,
                password: password
            };

            $.ajax({
                url: '/api/login',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(loginData),
                success: function(response) {
                    alert(response.message);
                    if (response.message === 'Inicio de sesión exitoso') {
                        // Redirigir al usuario a la página de perfil o donde desees
                        window.location.href = '/perfil';
                    }
                },
                error: function(error) {
                    console.error('Error al iniciar sesión:', error);
                    alert('Correo electrónico o contraseña incorrectos');
                }
            });
        }
    });

    $('#registerForm').on('submit', function (e) {
        e.preventDefault();
        let valid = true;

        // Validar nombre
        const name = $('#registerName').val();
        if (name.trim() === '') {
            $('#nameError').text('Por favor, ingrese su nombre completo.');
            valid = false;
        } else {
            $('#nameError').text('');
        }

        // Validar correo electrónico
        const email = $('#registerEmail').val();
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(email)) {
            $('#registerEmailError').text('Por favor, ingrese un correo electrónico válido.');
            valid = false;
        } else {
            $('#registerEmailError').text('');
        }

        // Validar contraseña
        const password = $('#registerPassword').val();
        if (password.length < 6) {
            $('#registerPasswordError').text('La contraseña debe tener al menos 6 caracteres.');
            valid = false;
        } else {
            $('#registerPasswordError').text('');
        }

        // Validar confirmación de contraseña
        const confirmPassword = $('#registerConfirmPassword').val();
        if (confirmPassword !== password) {
            $('#registerConfirmPasswordError').text('Las contraseñas no coinciden.');
            valid = false;
        } else {
            $('#registerConfirmPasswordError').text('');
        }

        if (valid) {
            // Si la validación es correcta, enviar los datos a la API
            const nuevoUsuario = {
                nombre: name,
                email: email,
                password: password
            };

            $.ajax({
                url: '/api/usuarios',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(nuevoUsuario),
                success: function(response) {
                    alert(response.message);
                    if (response.message === 'Usuario registrado con éxito') {
                        // Redirigir al usuario a la página de inicio de sesión o donde desees
                        window.location.href = '/login';
                    }
                },
                error: function(error) {
                    console.error('Error al registrar el usuario:', error);
                    $('#registerError').text(error.responseJSON.message);
                }
            });
        }
    });

    $('#contactForm').on('submit', function(e) {
        e.preventDefault();
        let valid = true;

        // Validar nombre
        const nombre = $('#nombre').val().trim();
        if (nombre === '') {
            $('#nombreError').text('Por favor, introduce tu nombre.');
            valid = false;
        } else {
            $('#nombreError').text('');
        }

        // Validar teléfono
        const telefono = $('#telefono').val().trim();
        const telefonoPattern = /^[\d\s-+()]+$/;
        if (!telefonoPattern.test(telefono)) {
            $('#telefonoError').text('Por favor, introduce un teléfono válido.');
            valid = false;
        } else {
            $('#telefonoError').text('');
        }

        // Validar correo electrónico
        const email = $('#email').val().trim();
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(email)) {
            $('#emailError').text('Por favor, introduce un correo electrónico válido.');
            valid = false;
        } else {
            $('#emailError').text('');
        }

        if (valid) {
            alert('Formulario enviado con éxito.');
            // Aquí puedes agregar la lógica para enviar el formulario al servidor
        }
    });

    $('#perfilForm').on('submit', function(e) {
        e.preventDefault();

        const telefono = $('#telefono').val();
        const email = $('#email').val();
        const direccion = $('#direccion').val();

        const datosActualizados = {
            telefono: telefono,
            email: email,
            direccion: direccion
        };

        $.ajax({
            url: '/api/actualizar_perfil',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(datosActualizados),
            success: function(response) {
                alert(response.message);
                // Puedes actualizar la interfaz o redirigir según lo que necesites
            },
            error: function(error) {
                console.error('Error al actualizar el perfil:', error);
            }
        });
    });

    $('#logoutButton').on('click', function() {
        $.ajax({
            url: '/logout',
            method: 'POST',
            success: function(response) {
                alert(response.message);
                window.location.href = '/';
            },
            error: function(error) {
                console.error('Error al cerrar sesión:', error);
            }
        });
    });
});
