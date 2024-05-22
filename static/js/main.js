document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/productos')
        .then(response => response.json())
        .then(data => {
            let productosContainer = document.getElementById('productos');
            productosContainer.innerHTML = '';
            data.forEach(producto => {
                let productoHTML = `
                <div class="col-md-4 mb-3">
                    <div class="card fondo border-custom">
                        <a href="HTML/productos/${producto.nombre.toLowerCase()}.html"><img src="${producto.foto}" class="card-img-top p-4"
                                alt="${producto.nombre} para Mascotas"></a>
                        <div class="card-body container">
                            <h5 class="card-title fw-bold">${producto.nombre}</h5>
                            <p class="card-text">${producto.descripcion}</p>
                            <p class="card-text"><strong>$${producto.precio}</strong></p>
                            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                                data-bs-target="#myModal">
                                <span title="Carrito">Agregar al Carrito
                                </span>
                            </button>
                        </div>
                    </div>
                </div>
                `;
                productosContainer.innerHTML += productoHTML;
            });
        })
        .catch(error => console.error('Error fetching productos:', error));
});
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/productos')
        .then(response => response.json())
        .then(data => {
            let productosContainer = document.getElementById('productosPopulares');
            productosContainer.innerHTML = '';

            // Limitar a los primeros 3 productos
            let productosLimitados = data.slice(0, 3);
             
            productosLimitados.forEach(producto => {
                let productoHTML = `
                <div class="col-md-4 mb-3">
                    <div class="card fondo border-custom">
                        <a href="HTML/productos/${producto.nombre.toLowerCase()}.html"><img src="${producto.foto}" class="card-img-top p-4"
                                alt="${producto.nombre} para Mascotas"></a>
                        <div class="card-body container">
                            <h5 class="card-title fw-bold">${producto.nombre}</h5>
                            <p class="card-text">${producto.descripcion}</p>
                            <p class="card-text"><strong>$${producto.precio}</strong></p>
                            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                                data-bs-target="#myModal">
                                <span title="Carrito">Agregar al Carrito
                                </span>
                            </button>
                        </div>
                    </div>
                </div>
                `;
                productosContainer.innerHTML += productoHTML;
            });
        })
        .catch(error => console.error('Error fetching productos:', error));
});
