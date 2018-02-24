# Take the items in this list of lists: 
# [[" Top Gun", "Risky Business", "Minority Report"], 
# [" Titanic", "The Revenant", "Inception"], 
# [" Training Day", "Man on Fire", "Flight"]] 
# and write them to a CSV file. 
# The data from each list should be a row in the file, 
# with each item in the list separated by a comma.

import os
import csv

new_dir = os.path.join("C:\\","Users","dapinon","Documents","Training","The Self-Taught Programmer","Chapter 9 - Files")
os.chdir(new_dir)

movie_list = [[" Top Gun", "Risky Business", "Minority Report"],
                 [" Titanic", "The Revenant", "Inception"], 
                 [" Training Day", "Man on Fire", "Flight"]] 

with open("movie_list2.csv","w") as f:
    w = csv.writer(f,
                   delimiter=",")

    for movie in movie_list:
        w.writerow(movie)

with open("movie_list2.csv","r") as f:
#    print(f.read(),end="")
    for line in f:
        print(line,end="")
