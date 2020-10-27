def test_delite_git_branch(app):
    app.session.login(username="boriska67", password="Tashkent@67")
    app.branch.delete_branch()
    app.session.logout()