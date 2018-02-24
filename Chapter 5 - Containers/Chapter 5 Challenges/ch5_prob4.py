# Write a program that lets the user ask your height, 
# favorite color, or favorite author, and returns the 
# result from the dictionary you created in the previous challenge.


my_dict = {"1":"5 ft 10 in",
           "2":"brown",
           "3":"brown",
           "4":"blue",
           "5":"Stepen King",
           "6":"GATTACA",
           "7":"Super Mario Kart"}


response = input("""what would you like to know about me? 

Options include:
----------------
1. height
2. hair color
3. eye color
4. favorite color
5. favorite author
6. favorite movie
7. favorite video game

Select a number, between 1 and 7, to find out: 
""")

if response in my_dict:
    print(my_dict[response])
else:
    print("That's an invalid response.")
    
