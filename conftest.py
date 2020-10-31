import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="boriska67", password="Tashkent@67")
        fixture.branch.open_project_page()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="boriska67", password="Tashkent@67")
            fixture.branch.open_project_page()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture