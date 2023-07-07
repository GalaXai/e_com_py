from productcatalog.product import Product
import uuid


class ProductCatalog:
    def __init__(self, product_storage):
        self.product_storage = product_storage

    def add_product(self, name, description) -> Product:
        product = Product(uuid.uuid4(), name, description)
        self.product_storage.add_product(product)
        return product

    def get_all_products(self):
        return self.product_storage.get_all_products()

    def get_product_by_uuid(self, product_uuid):
        return self.product_storage.get_product_by_uuid(product_uuid)

    def delete_product_by_uuid(self, product_uuid):
        self.product_storage.delete_product_by_uuid(product_uuid)

    def update_price(self, product_uuid, price):
        product = self.product_storage.get_product_by_uuid(product_uuid)
        product.set_price(price)
        self.product_storage.update_product(product)

    def assign_image(self, product_uuid, image):
        product = self.product_storage.get_product_by_uuid(product_uuid)
        product.set_image(image)
        self.product_storage.update_product(product)

    def publish_product(self, product_uuid):
        product = self.product_storage.get_product_by_uuid(product_uuid)
        if product.get_price() == 0:
            raise ValueError("Product price is 0")
        if product.get_image() is None:
            raise ValueError("There is no image for this product")

        product.set_online()
        self.product_storage.update_product(product)


    def get_all_published_products(self) -> list:
        return self.product_storage.get_all_published_products()
