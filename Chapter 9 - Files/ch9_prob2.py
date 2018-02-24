# Write a program that asks a user a question, and saves their answer to a file.

import os

new_dir = os.path.join("C:\\","Users","dapinon","Documents","Training","The Self-Taught Programmer","Chapter 9 - Files")
os.chdir(new_dir)

answer = input("What is your name? ")

with open("name.txt","a") as f:
    f.write("\nHello, " + answer + "!")

with open("name.txt","r") as f:
    print(f.read())
