import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class BranchHelper:

    def __init__(self, app):
        self.app = app

    def create(self, branch):
        wd = self.app.wd
        wd.find_element_by_css_selector("#branch-select-menu > .btn").click()
        wd.find_element_by_id("context-commitish-filter-field").click()
        wd.find_element_by_id("context-commitish-filter-field").send_keys(branch.branchname)
        time.sleep(1)
        wd.find_element_by_id("context-commitish-filter-field").send_keys(Keys.ENTER)
        time.sleep(1)
        wd.find_element_by_css_selector(".link-gray-dark:nth-child(1) > .text-gray-light").click()
        time.sleep(1)

        # TEST
        # w_el = wd.find_elements_by_css_selector('.branch-name')
        try:
            if len(wd.find_elements_by_link_text(branch.branchname)) > 0:
                print("New branch found")
        except NoSuchElementException:
            print("No element found")
        time.sleep(1)
        wd.find_element_by_link_text("python_training").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#dashboard-repos-container > #repos-container .source .d-inline-flex").click()

    def delete_branch(self, branch):
        wd = self.app.wd
        wd.find_element_by_css_selector(".link-gray-dark:nth-child(1) > .text-gray-light").click()
        time.sleep(1)
        try:
            if len(wd.find_elements_by_link_text(branch.branchname)) > 0:
                wd.find_element_by_css_selector(".Box:nth-child(2) .btn-link > .octicon").click()
                time.sleep(1)
        except NoSuchElementException:
                print("No element found")
        time.sleep(1)
        try:
            if len(wd.find_elements_by_css_selector(".Box:nth-child(2) .btn-link > .octicon")) > 0:
                print("Unable to delete " + branch.branchname)
        except NoSuchElementException:
            print(branch.branchname + " was deleted.")


    def open_gotofile_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Go to file").click()

    def gotofile(self):
        wd = self.app.wd
        wd.find_element_by_link_text("python_training").click()
        self.open_gotofile_page()
        wd.find_element_by_link_text("python_training").click()