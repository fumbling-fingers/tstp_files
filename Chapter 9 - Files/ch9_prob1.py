# Find a file on your computer and 
# print its contents using Python.

import os

os.chdir("C:\\Python\\")

with open("LICENSE.txt","r") as f:
    print(f.read())