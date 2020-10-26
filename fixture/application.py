import time

# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def sign_out(self):
        wd = self.wd
        # clicking dropdown
        wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link").click()
        # clicking sign out link
        wd.find_element_by_css_selector(".dropdown-signout").click()

    def create_new_branch(self, branch):
        wd = self.wd
        self.open_project_page()
        wd.find_element_by_css_selector("#branch-select-menu > .btn").click()
        wd.find_element_by_id("context-commitish-filter-field").click()
        wd.find_element_by_id("context-commitish-filter-field").send_keys(branch.branchname)
        time.sleep(1)
        wd.find_element_by_id("context-commitish-filter-field").send_keys(Keys.ENTER)

    def open_project_page(self):
        wd = self.wd
        wd.find_element_by_css_selector("#dashboard-repos-container > #repos-container .source .d-inline-flex").click()

    def open_login_page(self, sign_in_link):
        wd = self.wd
        wd.find_element_by_link_text(sign_in_link).click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page("https://github.com/")
        self.open_login_page(sign_in_link="Sign in")
        wd.find_element_by_id("login_field").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_name("commit").click()

    def open_home_page(self, starting_page):
        wd = self.wd
        wd.get(starting_page)
        # wd.set_window_size(1936, 1066)
        wd.maximize_window()

    def destroy(self):
        self.wd.quit()