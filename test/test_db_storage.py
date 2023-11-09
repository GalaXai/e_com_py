import unittest
import os
from productcatalog.product_catalog import ProductCatalog
from productcatalog.database_product_storage import SQLiteProductStorage

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test database for each test case
        self.db_file = 'test.db'
        self.product_catalog = ProductCatalog(SQLiteProductStorage(self.db_file))

    def tearDown(self):
        # Remove the test database file after each test case
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_AllowsToAddProduct(self):
        self.product_catalog.add_product("Product 1", "Description 1")
        self.assertEqual(len(self.product_catalog.get_all_products()), 1)

    def test_AllowsToAddMultipleProducts(self):
        self.product_catalog.add_product("Product 1", "Description 1")
        self.product_catalog.add_product("Product 2", "Description 2")
        self.assertEqual(len(self.product_catalog.get_all_products()), 2)

if __name__ == '__main__':
    unittest.main()
