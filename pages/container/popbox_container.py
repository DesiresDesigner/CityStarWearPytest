from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.container_object import ContainerObject
from pages.page_object import self_cachable

class PopboxContainer(ContainerObject):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

        # Init XPATH
        self.xpath['popbox_container_close_btn'] = "//div[@class='cbb-hide-box']"

#   Getters
    @self_cachable()
    def get_popbox_close_btn(self):
        return (WebDriverWait(self.root, 2)
                    .until(EC.element_to_be_clickable((By.XPATH, self.xpath["popbox_container_close_btn"]))))

#   Actions
    def click_popbox_close_btn(self):
        self.get_popbox_close_btn().click()

    #   Methods
    def close_popbox(self):
        self.click_popbox_close_btn()
        self.invalidate()

