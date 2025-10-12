class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, element):
        element.click()

    def send_keys(self, element, value):
        element.clear()
        element.send_keys(value)

    def get_text(self, element):
        return element.text

