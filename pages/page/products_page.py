from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.page_object import self_cachable
from pages.page_with_header_menu import PageWithHeaderMenu
from pages.container.product_container import ProductContainerForProductsPage

class ProductsPage(PageWithHeaderMenu):

    def __init__(self, driver_manager):
        super().__init__(driver_manager)

        #Init XPATH
        self.xpath['title_container'] = "//div[@class='catalog-sidebar__title']/span"
        self.xpath['products_container'] = "//div[@class='catalog-products ']"
        self.xpath['product_in_container'] = "./div[@class='catalog-product']"

        self.products = self.get_products()


#   Getters
    @self_cachable()
    def get_title_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["title_container"]))))

    @self_cachable()
    def get_products_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["products_container"]))))

    def get_products(self):
        products_container = self.get_products_container()
        product_containers_list = products_container.find_elements(By.XPATH, self.xpath["product_in_container"])
        products_objects = []
        for product in product_containers_list:
            products_objects.append(ProductContainerForProductsPage(self.driver_manager, product))
        return products_objects


#   Actions


#   Methods
    @self_cachable()
    def open_product(self, serial_number=None, name=None):
        product_to_open = None
        if serial_number:
            product_to_open = self.products[serial_number]
        elif name:
            for product in self.products:
                if product.get_name() == name:
                    product_to_open = product
        product_info = {"name": product_to_open.get_name(), "price": product_to_open.get_price()}
        product_to_open.open()
        return product_info

    def get_title(self):
        return self.get_title_container().text
