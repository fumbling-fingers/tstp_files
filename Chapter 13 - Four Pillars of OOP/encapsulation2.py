# encapsulation refers to two concepts: 

# 1. objects groups variables (state) and methods (for altering state 
# or doing caculations that use state) in a singe unit

# 2. hides a class's internal data to prevent the CLIENT (code outside
# the class that uses the object) from directly accessing it

# http://tinyurl.com/jtz28ha

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data() # creates an instance of the Data class with 'nums' list
print(data_one.nums)

data_one.nums[0] = 100 # changes value at index[0] from 1 to 100
print(data_one.nums)

data_two = Data() # creates a second instance of the Data class with 'nums' list
print(data_two.nums)

data_two.change_data(2, 100) # also changes value at index[2] from 3 to 100
print(data_two.nums)