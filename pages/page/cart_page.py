from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.page_with_header_menu import PageWithHeaderMenu
from pages.page_object import self_cachable
from pages.container.product_container import ProductContainerForCartPage


class CartPage(PageWithHeaderMenu):

    def __init__(self, driver_manager):
        super().__init__(driver_manager)

        #Init XPATH
        self.xpath['basket_list_container'] = "//div[@class='basket__list']"
        self.xpath['product_in_basket'] = "./div[contains(@class, 'basket__item bs-basket-item')]"
        self.xpath['total_price_before_promo_container'] = "//div[@class='basket-total-cost']"
        self.xpath['total_price_after_promo_container'] = "//div[@class='basket-summary__cost']"
        self.xpath['continue_ordering_btn'] = "//div[@class='form-control']/a"
        self.xpath['title_container'] = "//div[@id='bs-c-step-0']//h1[@class='custom-header']/div"

        self.products = self.get_products()


#   Getters
    @self_cachable()
    def get_basket_list_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["basket_list_container"]))))

    @self_cachable()
    def get_title_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["title_container"]))))

    def get_products(self):
        products_container = self.get_basket_list_container()
        product_containers_list = products_container.find_elements(By.XPATH, self.xpath["product_in_basket"])
        products_objects = []
        for product in product_containers_list:
            products_objects.append(ProductContainerForCartPage(self.driver_manager, product))
        return products_objects

    @self_cachable()
    def get_price_before_promo_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["total_price_before_promo_container"]))))

    @self_cachable()
    def get_price_after_promo_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["total_price_after_promo_container"]))))

    @self_cachable()
    def get_continue_ordering_btn(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["continue_ordering_btn"]))))

#   Actions
    def click_continue_ordering_btn(self):
        self.get_continue_ordering_btn().click()

#   Methods
    @self_cachable()
    def get_price_before_promo(self):
        return int(self.get_price_before_promo_container().text[0:-2].replace(" ", ""))

    @self_cachable()
    def get_price_after_promo(self):
        return int(self.get_price_after_promo_container().text[0:-2].replace(" ", ""))

    @self_cachable()
    def get_title(self):
        return self.get_title_container().text

    def continue_ordering(self):
        self.click_continue_ordering_btn()

