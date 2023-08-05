(() => {
    console.log("My store works tf tf");
})();
// TODO fix js

const getProducts=  () => {
    return fetch("/api/products")
    .then((res) => res.json())

}

const addToCart = (product_uuid) => {
    console.log("adding to cart");
    return fetch(`/api/add-to-cart/${product_uuid}`, {
        method: "POST",
        body: JSON.stringify({})
    }).then(response => response.json());
}
const createHtmlElementFromString = (template) => {
    let tmpElement = document.createElement('div');
    tmpElement.innerHTML = template.trim();
    return tmpElement.firstChild;
}

const createProductComponent = (product) => {
    const template = `
        <li class="product">
            <span>${product.name}</span>
            <div>
                <span>${product.price}</span>
            </div>
            <div>
                <img src="/static/images/${product.image}" height = "auto", width="auto" alt="">
            </div>
            <button
                class="product__add-to-cart"
                data-product-id="${product.uuid}">
                Add to cart
            </button>
        </li>
    `;
    return createHtmlElementFromString(template);
}

const initializeAddToCartHandler = (el) => {
    const btn = el.querySelector('button.product__add-to-cart');
    btn.addEventListener('click', () => {
        addToCart(btn.getAttribute('data-product-id'))
            .then(refreshCurrentOffer())
    });
    return el;
}

const getCurrentOffer = () => {
    console.log('i am going to get offer');
    return fetch("/api/get-current-offer")
        .then(response => response.json());
}
const refreshCurrentOffer = () => {
    console.log('i am going to refresh offer');
    const offerElement = document.querySelector('.cart');
    getCurrentOffer()
        .then(offer => {
            offerElement.querySelector('.total').textContent = `${offer.total} PLN`;
            offerElement.querySelector('.items_count').textContent = `${offer.items_count} items`;
        });
}


(async () => {
    console.log("It works :)");
    const productsList = document.querySelector('#productsList');
    const products = await getProducts();
    products
        .map(p => createProductComponent(p))
        .map(el => initializeAddToCartHandler(el))
        .forEach(el => productsList.appendChild(el));
    console.log("post get products");
})();