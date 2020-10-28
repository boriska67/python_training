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
        if self.is_logged_in_as(username):
            print("Logged as " + username)
            return True
        else:
            print("Error: Logged as NOT " + username + "!!!")
            return False

    # def is_logged_in(self):
    #     wd = self.app.wd
    #     return len(wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link").click()
        text = wd.find_element_by_css_selector(".user-profile-link > .css-truncate-target").text
        wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link").click()
        if text.find(username) != -1:
            return True
        else:
            return False

    def logout(self):
        wd = self.app.wd
        # clicking dropdown
        wd.find_element_by_css_selector(".js-feature-preview-indicator-container > .Header-link").click()
        # clicking sign out link
        wd.find_element_by_css_selector(".dropdown-signout").click()

    # def ensure_logout(self):
    #     wd = self.app.wd
    #     if self.is_logged_in():
    #         self.logout()

    # def ensure_login(self, username, password):
    #     wd = self.app.wd
    #     if self.is_logged_in():
    #         if self.is_logged_in_as(username):
    #             return
    #         else:
    #             self.logout()
    #     self.login(username, password)
