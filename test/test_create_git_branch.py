from model.branch import Branch

# """ This is how to execute test with pytest C:\Users\Boris\Documents\GitHub\python_training>pytest -k test_creategitbranch -v"""

def test_create_git_branch(app):
    app.branch.create(Branch(branchname="new"))

