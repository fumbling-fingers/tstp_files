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

movies = [[" Top Gun", "Risky Business", "Minority Report"],
                 [" Titanic", "The Revenant", "Inception"], 
                 [" Training Day", "Man on Fire", "Flight"]] 

with open("movie_list3.csv", "w") as csvfile:
    w = csv.writer(csvfile, delimiter=",")

    for movie_list in movies:
        w.writerow(movie_list)
        
with open("movie_list3.csv","r") as csvfile:
    print(csvfile.read())

