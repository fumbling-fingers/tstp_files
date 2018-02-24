import re

string = """Arizona 479, 501, 870. California 209, 213, 650."""

matches = re.findall("\d\d\d", string)
matches2 = re.findall("\d..", string)

print(matches)
print(matches2)