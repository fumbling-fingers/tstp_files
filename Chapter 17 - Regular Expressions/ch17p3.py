import re

string = "The ghost that says boo haunts the loo."

matches = re.findall(".oo", string)

print(matches)