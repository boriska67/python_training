
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.ie.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.branch import BranchHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.branch = BranchHelper(self)
        
    def open_home_page(self, starting_page):
        wd = self.wd
        wd.get(starting_page)
        # wd.set_window_size(1936, 1066)
        wd.maximize_window()

    def open_login_page(self, sign_in_link):
        wd = self.wd
        wd.find_element_by_link_text(sign_in_link).click()

    def destroy(self):
        self.wd.quit()