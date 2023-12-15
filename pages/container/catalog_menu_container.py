from selenium.webdriver.common.by import By
from pages.container_object import ContainerObject
from pages.page_object import self_cachable
from pages.container.catalog_item_container import CatalogItemContainer

class CatalogMenuContainer(ContainerObject):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

        # Init XPATH
        self.xpath['items_list'] = "//ul[@class='header-catalog__menu_list']/li"

        self.get_catalog_items_list()

#   Getters
    @self_cachable()
    def get_catalog_items_list(self):
        items_elements_list = self.root.find_elements(By.XPATH, self.xpath["items_list"])
        catalog_items_list = []
        for item in items_elements_list:
            catalog_item = CatalogItemContainer(self.driver_manager, item)
            catalog_items_list.append(catalog_item)

        return catalog_items_list

#   Actions

#   Methods
    def open_catalog_item_by_serial_number(self, serial_number):
        self.get_catalog_items_list()[serial_number].choose_item()

    def open_catalog_item_by_name(self, name):
        for serial_number, item in enumerate(self.get_catalog_items_list()):
            if item.get_name() == name:
                self.open_catalog_item_by_serial_number(serial_number)
                return



