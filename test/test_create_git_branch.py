from model.branch import Branch
import pytest
from data.branch import testdata  # this is for using with testdata see data\branch
# from data.branch import constant as testdata  # this is for using with testdata as constant see data\branch

# """ This is how to execute test with pytest C:\Users\Boris\Documents\GitHub\python_training>pytest -k test_creategitbranch -v"""

@pytest.mark.parametrize("branch", testdata)
def test_create_git_branch(app, branch):
    app.branch.create(branch)

