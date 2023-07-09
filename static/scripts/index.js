(() => {
    console.log("My store works tf tf");
})();
// TODO fix js

const getProducts=  () => {
    return fetch("/api/products")
    .then((res) => res.json())

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
                <img src="/static/images/${product.image} " high = "auto", with= "auto" alt="">
            </div>
            <button
                class="product__add-to-cart"
                data-product-id="${product.id}"
            >
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

(async () => {
    console.log("It works :)");
    const productsList = document.querySelector('#productsList');
    const products = await getProducts();
    products
        .map(p => createProductComponent(p))
        //.map(el => initializeAddToCartHandler(el))
        .forEach(el => productsList.appendChild(el));
    console.log("post get products");
})();