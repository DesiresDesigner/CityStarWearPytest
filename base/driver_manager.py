from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


driver_inits = {
    "chrome": {
        "service_path": '/usr/local/bin/chromedriver',
        "options": lambda: ChromeOptions(),

    }
}


class DriverManager:
    def __init__(self, driver_key, options=[]):
        self.service = Service(driver_inits[driver_key]["service_path"])

        driver_options = None
        if options:
            driver_options = driver_inits[driver_key]["options"]()
            for option in options:
                driver_options.add_experimental_option(*option)

        self.driver = webdriver.Chrome(service=self.service, options=driver_options)
        self.action = None

    def create_driver(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    def create_action_chain(self):
        self.action = ActionChains(self.driver)

    def close_driver(self):
        self.driver.close()

    def move_to_element(self, element):
        if self.action is None:
            self.create_action_chain()
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


