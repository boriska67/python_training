# Generated by Selenium IDE
import pytest
import time
from branch import Branch
import json
from application import Application
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_creategitbranch(app):
    app.login(username="boriska67", password="Tashkent@67")
    app.create_new_branch(Branch(branchname="new"))
    app.sign_out()


