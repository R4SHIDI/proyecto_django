$(document).ready(function() {
    $("#form").on("submit", function(event) {
        // Evitar el envío del formulario
        event.preventDefault();

        // Limpiar mensajes de error anteriores
        $(".error1").text("");
        $(".error").text("");

        // Validar nombre de usuario
        var username = $("#asd1").val();
        if (username === "") {
            $(".error1").text("Por favor, ingrese su nombre de usuario.");
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
            this.submit();
            
        }
    });
});