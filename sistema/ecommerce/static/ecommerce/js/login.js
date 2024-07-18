$(document).ready(function() {
    $("#form").submit(function(event) {
        // Evitar el envío del formulario por defecto
        event.preventDefault();

        // Limpiar mensajes de error anteriores
        $(".error1").text("");
        $(".error").text("");

        // Validar nombre de usuario
        var username = $("#asd1").val().trim(); // Obtener valor y quitar espacios en blanco
        if (username === "") {
            $(".error1").text("Por favor, ingrese su nombre de usuario.");
        } else if (!/^[A-Za-z]+$/.test(username)) {
            $(".error1").text("El nombre de usuario no debe contener números.");
        }

        // Validar contraseña
        var password = $("#password2").val();
        if (password === "") {
            $(".error").text("Por favor, ingrese su contraseña.");
        } else if (password.length < 6) {
            $(".error").text("La contraseña debe tener al menos 6 caracteres.");
        }

        // Si no hay errores, enviar el formulario
        if ($(".error1").text() === "" && $(".error").text() === "") {
            $("#form")[0].submit(); // Enviar el formulario
        }
    });
});
