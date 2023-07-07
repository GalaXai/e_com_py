from abc import abstractmethod, ABC


class ProductStorage(ABC):

    @abstractmethod
    def add_product(self, product):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def get_all_products(self):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def get_product_by_uuid(self, uuid):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def delete_product_by_uuid(self, uuid):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def update_product(self, product):
        raise NotImplementedError("Please Implement this method")

    @property
    @abstractmethod
    def get_all_published_products(self) -> dict:
        raise NotImplementedError("Please Implement this method")
