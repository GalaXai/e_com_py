from flask import Flask, render_template, jsonify
from sales.cart.cart import Cart
from productcatalog.product_catalog import ProductCatalog
from productcatalog.hashmap_product_storage import HashProductStorage
from requests import request

app = Flask(__name__)

# TODO
# This is a temporary solution to make the app work for a demo
# Create empty cart cart
cart = Cart()

product_catalog = ProductCatalog(HashProductStorage())
product_catalog.add_product("Product 1", "Description 1")
product_catalog.add_product("Product 2", "Description 2")
product_catalog.add_product("Product 3", "Description 3")
images = ["ramotka.jpg", "futura.jpg", "audiotele.jpg"]
for i, product in enumerate(product_catalog.get_all_products()):
    # give each product a price and image
    product_catalog.update_price(product.get_uuid(), 100 * (i + 1))
    product_catalog.assign_image(product.get_uuid(), images[i])
    # publish each product
    product_catalog.publish_product(product.get_uuid())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/products', methods=['GET'])
def get_products():
    products = product_catalog.get_all_products()
    products_for_api = []
    for product in products:
        products_for_api.append({
            'uuid': product.get_uuid(),
            'name': product.get_name(),
            'description': product.get_desc(),
            'price': product.get_price(),
            'image': product.get_image(),
            'online': product.get_online()
        })
    return jsonify(products_for_api)

@app.route('/api/add-to-cart/<product_uuid>', methods=['POST'])
def add_to_cart(product_uuid):
    # Process the received data and the productId
    product = product_catalog.get_product_by_uuid(product_uuid)
    cart.add_product(product,quantity=1)
    # Return a JSON response
    response = {
        'status': 'success',
        'message': f'Product with ID {product_uuid} added to cart successfully.'
    }
    return jsonify(response)

@app.route('/api/get-current-offer', methods=['GET'])
def get_current_offer():
    print(cart)
    print("get_current_offer", cart.get_total(), cart.get_items_count())
    response = {
        'total': cart.get_total(),
        'items_count': cart.get_items_count(),
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
