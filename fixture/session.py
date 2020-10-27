class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page("https://github.com/")
        self.app.open_login_page(sign_in_link="Sign in")
        wd.find_element_by_id("login_field").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_name("commit").click()


    def logout(self):
        wd = self.app.wd
        # clicking dropdown
        wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link").click()
        # clicking sign out link
        wd.find_element_by_css_selector(".dropdown-signout").click()