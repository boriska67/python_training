from model.branch import Branch

def test_delete_git_branch(app):
    app.branch.delete_branch(Branch(branchname="new"))