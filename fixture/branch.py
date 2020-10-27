import time
from selenium.webdriver.common.keys import Keys

class BranchHelper:

    def __init__(self, app):
        self.app = app

    def create(self, branch):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("#branch-select-menu > .btn").click()
        wd.find_element_by_id("context-commitish-filter-field").click()
        wd.find_element_by_id("context-commitish-filter-field").send_keys(branch.branchname)
        time.sleep(1)
        wd.find_element_by_id("context-commitish-filter-field").send_keys(Keys.ENTER)

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#dashboard-repos-container > #repos-container .source .d-inline-flex").click()

    def delete_branch(self):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector(".link-gray-dark:nth-child(1) > .text-gray-light").click()
        time.sleep(1)
        wd.find_element_by_css_selector(".Box:nth-child(2) .btn-link > .octicon").click()
        time.sleep(1)