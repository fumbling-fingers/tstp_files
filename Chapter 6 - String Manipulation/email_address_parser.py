# The goal of this program is to read a list of names and e-mails from a file
# write into two separate columns the name and e-mail address

list_of_names = "David Pinon <David.Pinon@microsoft.com>; Greg Staska <gstaska@microsoft.com>; Lee Progl <leep@microsoft.com>; John Kim <kimjohn@microsoft.com>; Kevin Langston <Kevin.Langston@microsoft.com>; Jerry Gonzalez <Gerardo.Gonzalez@microsoft.com>"
print("")

# splits string of e-mails  
updated_list = list_of_names.split(";")
print(updated_list) # creates list from string

print("\n")

for name in updated_list:
    print(name)   