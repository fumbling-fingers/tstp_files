# Take the list [" The", "fox", "jumped", "over", "the", "fence", "."]
# and turn it into a grammatically correct string. There should be a
# space between each word, but no space between the word fence and the
# period that follows it. (Don't forget, you learned a method that turns
# a list of strings into a single string.)

words =  [" The", "fox", "jumped", "over", "the", "fence", "."]

sentence = " ".join(words)

sentence = sentence.replace("fence .","fence.")
sentence = sentence.replace(" The","The")

print(sentence)

# another way to solve this is to use the slice and concatenate
# methods on the string


# fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
# fox = " ".join(fox)
# fox = fox[0: -2] + "."
# print(fox)
