'''

P3-3 Exercise: Count Unique Characters
Problem Statement
Given a string, count how many unique characters appear in this string, and return the number.

Can you solve it in a linear time complexity O(n)? Hint: Use a dictionary instead of nested loops.

Example 1:


word = "ssahua"

# output: 4
# The four unique characters are "s", "a", "h", "u"
print(countChar(word))
Example 2:


word = "kk"

# output: 1
# The unique character is "k"
print(countChar(word))
'''


word = "ssahua"
def countChar(sentence):
    # return how many unique elements are in it
    sent = set()
    for element in sentence:
        sent.add(element)
    return len(sent)
# output: 4
# The four unique characters are "s", "a", "h", "u"
print(countChar(word))


'''
P4-3 Exercise: Check Duplicates in a List (Revisited)
Problem Statement
Write a function that checks whether any value appears more than twice in a list. Return True if there are duplicate elements, and return False if every element is distinct.

Can you come up with a solution with O(n) time complexity using the set data structure?

Example 1:


numbers = [5, 2, 9, 8, 1, 10]

# output: False
print(containDuplicates(numbers))
Example 2:


numbers = [4, 12, 91, 63, 4, 80, 80]

# output: True
print(containDuplicates(numbers))

'''
numbers = [4, 12, 91, 63, 80, 80]

def Duplicate(num):
    numb = set()
    for i in num:
        if i in numb:
            return True
        numb.add(i)
    return False
        
        

print(Duplicate(numbers))    