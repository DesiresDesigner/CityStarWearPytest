from pages.container_object import ContainerObject
from pages.page_object import PageObject, self_cachable

class CatalogItemContainer(ContainerObject):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager, root)

#   Getters

#   Actions

#   Methods
    @self_cachable()
    def get_name(self):
        return self.root.text

    def choose_item(self):
        self.root.click()




