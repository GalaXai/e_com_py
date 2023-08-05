import unittest
from productcatalog import product
from sales.cart.cart import Cart
from productcatalog.product_catalog import ProductCatalog
from productcatalog.hashmap_product_storage import HashProductStorage

class MyTestCase(unittest.TestCase):
    def prep_product_catalog(self) -> ProductCatalog:
        product_catalog = ProductCatalog(HashProductStorage())
        product_catalog.add_product("Product 1", "Description 1")
        product_catalog.add_product("Product 2", "Description 2")
        product_catalog.add_product("Product 3", "Description 3")
        images = ['ramotka.jpg', 'futura.jpg', 'audiotele.jpg']
        for i, product in enumerate(product_catalog.get_all_products()):
            # give each product a price and image
            product_catalog.update_price(product.get_uuid(), 100 * (i + 1))
            product_catalog.assign_image(product.get_uuid(), images[i])
            # publish each product
            product_catalog.publish_product(product.get_uuid())
        return product_catalog

    def test_something(self):
        self.assertEqual(True, False)

    def test_add_to_cart(self):
        productcatalog = self.prep_product_catalog()
        cart = Cart()
        products = productcatalog.get_all_products()
        product = products[0]
        cart.add_product(product, 1)
        self.assertEqual(cart.get_items_count(), 1)
    def test_get_total_value(self):
        productcatalog = self.prep_product_catalog()
        cart = Cart()
        products = productcatalog.get_all_products()
        product = products[0]
        cart.add_product(product, 1)
        self.assertEqual(cart.get_total(), 100)





if __name__ == '__main__':
    unittest.main()
