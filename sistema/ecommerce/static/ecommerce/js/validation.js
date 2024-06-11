 //JQUERY PARA FORMULARIO 
 // Espera a que el DOM esté completamente cargado
 $(document).ready(function() {
    // Manejador de envío del formulario
    $('form').submit(function(event) {
      // Verificar si el formulario es válido
      if (!this.checkValidity()) {
        event.preventDefault(); // Detener el envío del formulario si no es válido
        event.stopPropagation();
      }
      $(this).addClass('was-validated'); // Agregar clases de validación según Bootstrap
    });
  });

  

  //FUNCIÓN JQUERY  DESPLAZAMIENTO SUAVE
  // Espera a que el DOM esté completamente cargado
  $(document).ready(function() {
    $('a.nav-link').on('click', function(event) {
      var href = $(this).attr('href');
      if (href.startsWith('#')) {
        var target = $(href);
        if (target.length) {
          event.preventDefault();
          $('html, body').stop().animate({
            scrollTop: target.offset().top - 70 // Ajuste para compensar la barra de navegación fija
          }, 1000);
        }
      }
    });
  




    // Función para cambiar el color de fondo al pasar el cursor
    $('.card').hover(function() {
        $(this).css('background-color', '#000000'); // Cambia a color negro 
    }, function() {
        $(this).css('background-color', ''); // Restaurar el color de fondo original
    });
});

 



