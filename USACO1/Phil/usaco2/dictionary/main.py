'''
Problem 5

Write a program that stores all keys in a dictionary into a list.

Example:

python
dict = { "Andrew": 27, "Kevin": 35, "Rapi": 18, "Dola": 29 }

# expected values in the list
keys = ["Andrew", "Kevin", "Rapi", "Dola"]
'''
dict = { "Andrew": 27, "Kevin": 35, "Rapi": 18, "Dola": 29 }

# expected values in the list
key = dict.keys()
print(key)

d = {}      # this is one way of creating an empty dictionary

# dictionary with string keys
# here we have our string "John", "Alex", and "Chris" as keys
# and integers 90, 96, and 87 as values
grades = { "John": 90, "Alex": 96, "Chris": 87 }

grades["Phil"] = -1
grades["Fooj"] = 100
print(grades)


Problem 6

Write a program that flips the keys and its associated values. You can assume there will be no duplicate values.

Example:

python
dict = { "Andrew": 27, "Kevin": 35, "Rapi": 18, "Dola": 29 }

# expected dictionary
flipped = { 27: "Andrew", 35: "Kevin", 18: "Rapi", 29: "Dola" }