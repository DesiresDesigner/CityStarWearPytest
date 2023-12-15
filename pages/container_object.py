from pages.page_object import PageObject


class ContainerObject(PageObject):

    def __init__(self, driver_manager, root):
        super().__init__(driver_manager)
        self.root = root
