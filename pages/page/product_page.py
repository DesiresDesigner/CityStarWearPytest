from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.page_object import self_cachable
from pages.page_with_header_menu import PageWithHeaderMenu

class ProductPage(PageWithHeaderMenu):

    def __init__(self, driver_manager):
        super().__init__(driver_manager)

        # Init XPATH
        self.xpath['title_container'] = "//h1[@class='bs-product-title']"
        self.xpath['price_container'] = "//div[@class='catalog-card__price']/div[@class='price']"
        self.xpath['add_to_cart_btn'] = "//div[@class='catalog-card__buy']/a"


#   Getters
    @self_cachable()
    def get_title_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["title_container"]))))

    @self_cachable()
    def get_price_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["price_container"]))))

    @self_cachable()
    def get_add_to_cart_btn(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["add_to_cart_btn"]))))

#   Actions
    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()

#   Methods
    def add_to_cart(self):
        self.click_add_to_cart_btn()

    @self_cachable()
    def get_name(self):
        return self.get_title_container().text

    @self_cachable()
    def get_price(self):
        return int(self.get_price_container().text[0:-2].replace(' ', ''))