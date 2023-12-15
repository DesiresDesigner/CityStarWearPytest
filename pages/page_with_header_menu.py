from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.container.catalog_menu_container import CatalogMenuContainer
from pages.page_object import PageObject, self_cachable

class PageWithHeaderMenu(PageObject):
    def __init__(self, driver_manager):
        super().__init__(driver_manager)
        self.catalog_menu_container = None

        # Init XPATH
        self.xpath['header_container'] = "//div[@class='header-wrapper']"
        self.xpath['catalog_menu_btn'] = ".//a[@class='header-catalog__link']"
        self.xpath['catalog_menu_container'] = "//div[@class='header-catalog__menu_item']"
        self.xpath['cart_btn'] = ".//a[@class='header-basket']"

#   Getters
    @self_cachable()
    def get_header_container(self):
        return (WebDriverWait(self.driver_manager.driver, 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["header_container"]))))
    @self_cachable()
    def get_catalog_menu_btn(self):
        return (WebDriverWait(self.get_header_container(), 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["catalog_menu_btn"]))))

    @self_cachable()
    def get_cart_btn(self):
        return (WebDriverWait(self.get_header_container(), 5)
                .until(EC.element_to_be_clickable((By.XPATH, self.xpath["cart_btn"]))))

#   Actions
    def click_catalog_menu_btn(self):
        self.get_catalog_menu_btn().click()

    def click_cart_btn(self):
        self.get_cart_btn().click()

#   Methods
    def open_catalog_menu(self):
        self.click_catalog_menu_btn()
        catalog_menu_container = (WebDriverWait(self.driver_manager.driver, 5)
                                  .until(EC.element_to_be_clickable((By.XPATH, self.xpath["catalog_menu_container"]))))
        self.catalog_menu_container = CatalogMenuContainer(self.driver_manager, catalog_menu_container)

    def choose_catalog_menu_item(self, serial_number=None, name=None):
        if serial_number:
            self.catalog_menu_container.open_catalog_item_by_serial_number(serial_number)
        elif name:
            self.catalog_menu_container.open_catalog_item_by_name(name)

    def open_cart(self):
        self.click_cart_btn()