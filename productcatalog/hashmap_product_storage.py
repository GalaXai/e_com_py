from productcatalog.product_storage import ProductStorage


class HashProductStorage(ProductStorage):
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.get_uuid()] = product

    def get_all_products(self) -> list:
        return [product for product in self.products.values()]

    def get_product_by_uuid(self, uuid):
        return self.products.get(uuid)

    def delete_product_by_uuid(self, uuid):
        del self.products[uuid]

    def update_product(self, product):
        self.products[product.get_uuid()] = product


    def get_all_published_products(self) -> list:
        return [product for product in self.products.values() if product.get_online()]
