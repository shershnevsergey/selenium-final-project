from selenium.webdriver import Remote as RemoteWebdriver

class BasePage():
    def __init__(self, browser: RemoteWebdriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
