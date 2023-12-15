import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.page_with_header_menu import PageWithHeaderMenu
from pages.page_object import self_cachable
from pages.container.product_container import ProductContainerForOrderPage

class OrderPage(PageWithHeaderMenu):

    def __init__(self, driver_manager):
        super().__init__(driver_manager)

        #Init XPATH
        self.xpath['order_list_container'] = "//div[@class='basket-order__wrapper']"
        self.xpath['product_in_order'] = "./div[@class='basket-order__items']/div[contains(@class, 'basket-order__item')]"
        self.xpath['prices_before_delivery'] = "//div[@class='basket-order__total']/div[@class='basket-order__total-item']/span"
        self.xpath['total_price_after_delivery_container'] = "//div[@class='basket-order__summary']/span[@class='full-sum']"
        self.xpath['loader'] = "//div[@class='preloader' and @style='display: none;']"
        self.xpath['title_container'] = "//div[@id='bs-c-step-1']//h1[@class='custom-header']/div"

        (WebDriverWait(self.driver_manager.driver, 10)
         .until(EC.presence_of_element_located((By.XPATH, self.xpath['loader']))))

        self.products = self.get_products()

#   Getters
    @self_cachable()
    def get_order_list_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["order_list_container"]))))

    @self_cachable()
    def get_title_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["title_container"]))))

    def get_products(self):
        products_container = self.get_order_list_container()
        product_containers_list = products_container.find_elements(By.XPATH, self.xpath["product_in_order"])
        products_objects = []
        for product in product_containers_list:
            products_objects.append(ProductContainerForOrderPage(self.driver_manager, product))
        return products_objects


    # XXX: selenium doesnt support WebDriverWait on multiple elements, even if we select only one
    @self_cachable()
    def get_price_before_delivery_container(self):
        elements = self.driver_manager.driver.find_elements(By.XPATH, self.xpath["prices_before_delivery"])
        return elements[1]

    @self_cachable()
    def get_delivery_price_container(self):
        elements = self.driver_manager.driver.find_elements(By.XPATH, self.xpath["prices_before_delivery"])
        return elements[3]

    @self_cachable()
    def get_price_after_delivery_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["total_price_after_delivery_container"]))))


#   Actions

#   Methods
    @self_cachable()
    def get_price_before_delivery(self):
        return int(self.get_price_before_delivery_container().text[0:-2].replace(" ", ""))

    @self_cachable()
    def get_title(self):
        return self.get_title_container().text

    @self_cachable()
    def get_delivery_price(self):
        acceptable_tries = 3
        price = "Загрузка"
        for i in range(acceptable_tries):
            price = self.get_delivery_price_container().text
            if "Загрузка" in price:
                time.sleep(4)
                continue
            break
        return int(price[0:-2].replace(" ", ""))

    @self_cachable()
    def get_price_after_delivery(self):
        acceptable_tries = 3
        price = "Загрузка"
        for i in range(acceptable_tries):
            price = self.get_price_after_delivery_container().text
            if "Загрузка" in price:
                time.sleep(4)
                continue
            break
        return int(price[0:-2].replace(" ", ""))


