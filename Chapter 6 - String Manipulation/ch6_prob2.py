# Write a program that collects two strings from a user,
# inserts them into the string "Yesterday I wrote a
# [response_one]. I sent it to [response_two]!" and prints
# a new string.

noun = input("Enter a noun : ")
name = input("Enter another name: ")

sentence = ("Yesterday I wrote a " + noun + ". I sent it to " + name + "!")

# should solve using the 'format' method
sentence2 = "Yesterday I wrote a {}. I sent it to {}!".format(noun,name)

print(sentence)
print(sentence2)
