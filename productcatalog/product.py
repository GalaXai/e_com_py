class Product:
    def __init__(self, uuid: object, name: str, desc: str) -> None:
        self.__UUID = uuid
        self.__NAME = name
        self.__DESC = desc
        self.__price = 0
        self.__online = False
        self.__image = None

    "setters"

    def set_price(self, price):
        self.__price = price

    def set_online(self):
        self.__online = True

    def set_offline(self):
        self.__online = False

    def set_image(self, image):
        self.__image = image

    "getters"

    def get_uuid(self):
        return self.__UUID

    def get_name(self):
        return self.__NAME

    def get_desc(self):
        return self.__DESC

    def get_price(self):
        return self.__price

    def get_online(self):
        return self.__online

    def get_image(self):
        return self.__image
