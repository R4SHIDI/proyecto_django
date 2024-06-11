function initMap() {
    var location = {lat: -33.36600112915039, lng: -70.67826843261719}; // Coordenadas de ejemplo
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15, // Ajusta el nivel de zoom según sea necesario
      center: location
    });
  
    var marker = new google.maps.Marker({
      position: location,
      map: map
    });
  }
  
  // Inicializa el mapa cuando se carga la página
  window.onload = initMap;
  