import unittest
from productcatalog.product_catalog import ProductCatalog
from productcatalog.hashmap_product_storage import HashProductStorage


# noinspection DuplicatedCode
class TestProductCatalog(unittest.TestCase):
    def _init_poroduct_catalog(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product_catalog.add_product("Product 1", "Description 1")
        return product_catalog
    def test_AllowsToAddProduct(self):
        product_catalog = self._init_poroduct_catalog()
        self.assertEqual(len(product_catalog.get_all_products()), 1)

    def test_AllowsToGetProductByUUID(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        self.assertEqual(product_catalog.get_product_by_uuid(product.get_uuid()), product)

    def test_AllowsToDeleteProductByUUID(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.delete_product_by_uuid(product.get_uuid())
        self.assertEqual(len(product_catalog.get_all_products()), 0)

    def test_AllowsToUpdatePrice(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.update_price(product.get_uuid(), 100)
        self.assertEqual(product.get_price(), 100)

    def test_AllowsToAssignImage(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.assign_image(product.get_uuid(), "image.png")
        self.assertEqual(product.get_image(), "image.png")

    def test_AllowsToPublishProduct(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.update_price(product.get_uuid(), 100)
        product_catalog.assign_image(product.get_uuid(), "image.png")
        product_catalog.publish_product(product.get_uuid())
        self.assertEqual(product.get_online(), True)

    def test_DoesNotAllowToPublishProductWithPriceZero(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.update_price(product.get_uuid(), 0)
        with self.assertRaises(ValueError):
            product_catalog.publish_product(product.get_uuid())

    def test_DoesNotAllowToPublishProductWithoutImage(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.update_price(product.get_uuid(), 100)
        with self.assertRaises(ValueError):
            product_catalog.publish_product(product.get_uuid())

    def test_AllowsToGetAllPublishedProducts(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product1 = product_catalog.add_product("Product 1", "Description 1")
        product2 = product_catalog.add_product("Product 2", "Description 2")
        product_catalog.update_price(product1.get_uuid(), 100)
        product_catalog.assign_image(product1.get_uuid(), "image1.png")
        product_catalog.publish_product(product1.get_uuid())
        product_catalog.update_price(product2.get_uuid(), 200)
        product_catalog.assign_image(product2.get_uuid(), "image2.png")
        self.assertEqual(len(product_catalog.get_all_published_products()), 1)
        self.assertEqual(product_catalog.get_all_published_products()[0], product1)

    def test_DoesAllowToGetProductsFromEmtpyCatalog(self):
        product_catalog = ProductCatalog(HashProductStorage())
        self.assertEqual(len(product_catalog.get_all_published_products()), 0)

    def test_ItCreatesEmptyCatalog(self):
        product_catalog = ProductCatalog(HashProductStorage())
        self.assertEqual(len(product_catalog.get_all_products()), 0)

    def test_ItAllowsToLoadProductDetails(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product = product_catalog.add_product("Product 1", "Description 1")
        product_catalog.update_price(product.get_uuid(), 100)
        product_catalog.assign_image(product.get_uuid(), "image1.png")
        product_catalog.publish_product(product.get_uuid())
        loaded_product = product_catalog.get_product_by_uuid(product.get_uuid())
        self.assertEqual(product.get_price(), loaded_product.get_price())
        self.assertEqual(product.get_image(), loaded_product.get_image())
        self.assertEqual(product.get_online(), loaded_product.get_online())
        self.assertEqual(product.get_name(), loaded_product.get_name())
        self.assertEqual(product.get_desc(), loaded_product.get_desc())

    def test_ItAllowsToLoadAllProducts(self):
        product_catalog = ProductCatalog(HashProductStorage())
        product1 = product_catalog.add_product("Product 1", "Description 1")
        product2 = product_catalog.add_product("Product 2", "Description 2")
        product_catalog.update_price(product1.get_uuid(), 100)
        product_catalog.assign_image(product1.get_uuid(), "image1.png")
        product_catalog.publish_product(product1.get_uuid())
        product_catalog.update_price(product2.get_uuid(), 200)
        product_catalog.assign_image(product2.get_uuid(), "image2.png")
        self.assertEqual(len(product_catalog.get_all_products()), 2)


if __name__ == '__main__':
    unittest.main()
