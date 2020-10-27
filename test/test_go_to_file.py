def test_create_git_branch(app):
    app.session.login(username="boriska67", password="Tashkent@67")
    app.branch.gotofile()
    app.session.logout()