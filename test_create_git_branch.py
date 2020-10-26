# Generated by Selenium IDE
import pytest
from branch import Branch
from application import Application

# """ This is how to execute test with pytest C:\Users\Boris\Documents\GitHub\python_training>pytest -k test_creategitbranch -v"""
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_creategitbranch(app):
    app.login(username="boriska67", password="Tashkent@67")
    app.create_new_branch(Branch(branchname="new"))
    app.sign_out()


