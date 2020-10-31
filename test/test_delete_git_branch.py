from model.branch import Branch
import pytest

# Line below adding ability to run with parameters
# from data.branch import testdata
# This line adding ability to run with parameters as constant
from data.branch import constant as testdata


@pytest.mark.parametrize("branch", testdata)
def test_delete_git_branch(app, branch):
    app.branch.delete_branch(branch)  # (Branch(branchname="new"))