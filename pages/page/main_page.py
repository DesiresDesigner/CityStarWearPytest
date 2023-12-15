from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.page_with_header_menu import PageWithHeaderMenu
from pages.container.popbox_container import PopboxContainer

class MainPage(PageWithHeaderMenu):

    def __init__(self, driver_manager):
        super().__init__(driver_manager)

        #Init XPATH
        self.xpath['popbox_container'] = "//div[@class='bs-overlay-popbox']"

        self.popbox_container = self.get_popbox_container()


#   Getters
    def get_popbox_container(self):
        try:
            popbox_container = (WebDriverWait(self.driver_manager.driver, 2)
                    .until(EC.element_to_be_clickable((By.XPATH, self.xpath["popbox_container"]))))
            return PopboxContainer(self.driver_manager, popbox_container)
        except TimeoutException:
            return None

#   Actions

#   Methods
    def close_popbox_if_exit(self):
        if self.popbox_container:
            self.popbox_container.close_popbox()
            self.popbox_container = None
            print("LOG: popup closed")
