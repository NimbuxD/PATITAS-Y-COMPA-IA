document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/productos')
        .then(response => response.json())
        .then(data => {
            let productosContainer = document.getElementById('productos');
            productosContainer.innerHTML = '';
            data.forEach(producto => {
                let descuento = producto.precio * 0.05;
                let precioConDescuento = producto.precio - descuento;
                let productoHTML = `
                <div class="col-md-4 mb-3">
                    <div class="card fondo border-custom">
                        <a href="/producto/${producto.id}"><img src="${producto.foto}" class="card-img-top p-4"
                                alt="${producto.nombre} para Mascotas"></a>
                        <div class="card-body container">
                            <h5 class="card-title fw-bold">${producto.nombre}</h5>
                            <p class="card-text">${producto.descripcion}</p>
                            <p class="card-text"><strong>$${producto.precio}</strong></p>
                            <button type="button" class="btn btn-primary add-to-cart" data-id="${producto.id}" data-name="${producto.nombre}" data-price="${producto.precio}">
                                Agregar al Carrito
                            </button>
                        </div>
                    </div>
                </div>
                `;
                productosContainer.innerHTML += productoHTML;
            });

            attachAddToCartEvent();
        })
        .catch(error => console.error('Error al obtener productos:', error));

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
                        <a href="/producto/${producto.id}"><img src="${producto.foto}" class="card-img-top p-4"
                                alt="${producto.nombre} para Mascotas"></a>
                        <div class="card-body container">
                            <h5 class="card-title fw-bold">${producto.nombre}</h5>
                            <p class="card-text">${producto.descripcion}</p>
                            <p class="card-text"><strong>$${producto.precio}</strong></p>
                            <button type="button" class="btn btn-primary add-to-cart" data-id="${producto.id}" data-name="${producto.nombre}" data-price="${producto.precio}" data-foto="${producto.foto}">
                                Agregar al Carrito
                            </button>
                        </div>
                    </div>
                </div>
                `;
                productosContainer.innerHTML += productoHTML;
            });

            attachAddToCartEvent();
        })
        .catch(error => console.error('Error al obtener productos:', error));

    function attachAddToCartEvent() {
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', function () {
                const productId = this.getAttribute('data-id');
                const productName = this.getAttribute('data-name');
                const productPrice = this.getAttribute('data-price');
                const productFoto = this.getAttribute('data-foto');

                console.log(`Agregando al carrito: ID=${productId}, Nombre=${productName}, Precio=${productPrice}, Foto=${productFoto}`); // Log para depuración

                fetch('/add_to_cart', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        product_id: productId,
                        product_name: productName,
                        product_price: productPrice,
                        product_foto: productFoto
                    })
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Respuesta del servidor:', data); // Log para depuración
                        updateCart();
                    })
                    .catch(error => console.error('Error al agregar producto al carrito:', error));
            });
        });
    }

    function updateCart() {
        fetch('/get_cart')
            .then(response => response.json())
            .then(cart => {
                let cartHtml = '';
                let total = 0;

                cart.forEach(item => {
                    cartHtml += `
                        <div class="row container d-flex justify-content-center mx-0">
                            <div class="col-12 text-center fw-bold">${item.product_name}</div>
                            <div class="col-12 text-center"><img src="${item.product_foto}" alt="${item.product_name}" class="img-fluid" style="max-width: 50px;"></div>
                            <div class="col-6">Precio</div>
                            <div class="col-6 text-center fw-bold">$${item.product_price}</div>
                        </div>
                        <hr>
                    `;
                    total += parseFloat(item.product_price);
                });

                document.getElementById('cartItems').innerHTML = cartHtml;
                document.getElementById('totalPrice').innerText = `$${total.toFixed()}`;
            })
            .catch(error => console.error('Error al actualizar carrito:', error));
    }

    updateCart();
});