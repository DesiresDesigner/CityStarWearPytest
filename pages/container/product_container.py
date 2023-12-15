from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.container_object import ContainerObject
from pages.page_object import self_cachable

class ProductContainer(ContainerObject):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

    #   Getters
    @self_cachable()
    def get_name_container(self):
        return (WebDriverWait(self.root, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["name_container"]))))

    @self_cachable()
    def get_price_container(self):
        try:
            container = (WebDriverWait(self.root, 5)
                         .until(EC.element_to_be_clickable((By.XPATH, self.xpath["price_container"]))))
        except TimeoutException:
            container = None
        return container

    #   Actions

    #   Methods
    @self_cachable()
    def get_name(self):
        return self.get_name_container().text

    @self_cachable()
    def get_price(self):
        price_container = self.get_price_container()
        price = 0
        if price_container:
            price = price_container.text[0:-2].replace(' ', '')
        return int(price)

    def open(self):
        self.driver_manager.move_to_element(self.get_name_container())
        self.get_name_container().click()

class ProductContainerForProductsPage(ProductContainer):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

        # Init XPATH
        self.xpath['name_container'] = "./a[@class='catalog-product__title']"
        self.xpath['price_container'] = "./div[@class='catalog-product__price']"

    #   Getters

    #   Actions

    #   Methods

class ProductContainerForCartPage(ProductContainer):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

        # Init XPATH
        self.xpath['name_container'] = ".//a[@class='basket__title']"
        self.xpath['price_container'] = ".//span[@class='price']"

    #   Getters

    #   Actions

    #   Methods

class ProductContainerForOrderPage(ProductContainer):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

        # Init XPATH
        self.xpath['name_container'] = ".//a[@class='basket-order__title']"
        self.xpath['price_container'] = ".//span[@class='price']"
        self.xpath['old_price_container'] = ".//span[@class='price_old']"

#   Getters
    @self_cachable()
    def get_old_price_container(self):
        try:
            return (WebDriverWait(self.root, 5)
                    .until(EC.element_to_be_clickable((By.XPATH, self.xpath["old_price_container"]))))
        except TimeoutException:
            container = None
        return container

    @self_cachable()
    def get_old_price(self):
        price_container = self.get_new_price_container()
        price = 0
        if price_container:
            price = price_container.text[0:-2].replace(' ', '')
        return int(price)

#   Actions

#   Methods
