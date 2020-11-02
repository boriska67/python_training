from model.branch import Branch
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:", ["file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

f = "data/branch.json"

for o, a in opts:
    if o == "-f":
        f = a

testdata = [Branch(branchname="new"), Branch(branchname="mudak")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))