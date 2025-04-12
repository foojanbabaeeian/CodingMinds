# '''
# for i in range(5):
#     print("Phil is eating a pear")
    
    
    
# print()
# print()
# print()
# print()
# print()


# def eating(n):
#     if n == 0:
#         return 
#     else: 
#         print("Phil is eating a pear")
#         return eating(n-1)
        
# eating(5)
# '''
# '''
# nums = [6, 5, 4, 7, 7, 10, 7]

# for i in range(len(nums)):
#     print(nums[i])
# '''
# # nums = [6, 5, 4, 7, 7, 10, 7]
# # for i in range(len(nums)):
# #     print(nums[i])
    
# # You will have to write this code in recursion
# # def printNums(nums, index):
# #     if index == 0:
# #         print(nums[index])
# #         return
# #     printNums(nums, index-1)
# #     print(nums[index])
# #     return
        

# # printNums(nums, len(nums) - 1)


# # Factorial is product of every positve numver less than or equal to a given integer

# def factorial(n):
#     if n == 1: #base case, this is where rhe recursion call stops
#         return 1
#     else:
#         return n * factorial(n-1)
    
# def factorial_iterate(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# # output: 5040
# # print(factorial(7))
# # print(factorial_iterate(7))
# '''
# P6-2 Exercise: Fibonacci Sequence
# The fibonacci numbers are the numbers in the following sequence:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# Where the first two numbers are 0 and 1, with each subsequent number defined as the sum of the previous two numbers in the sequence.

# The 2 is found by adding the two numbers before it (1 + 1)
# The 3 is found by adding the two numbers before it (1 + 2)
# The 5 is (2 + 3)
# '''

# def feb(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#        return feb(n-1) + feb(n-2)
# print(feb(7))



### Problem 2
# Convert the following code from a recursive function into a loop.


# def factorial(n):
#     if (n <= 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# def factorial(n):
#     start = 1
#     for i in range(1, n+1):
#         start = start * i 
#     return start

# Convert the following code from a recursive function into a loop.

# def printElement(n):
#     if (n == 0):
#         return
#     else:
#         print("Hi there")
#         printElement(n - 1)
# # printElement(5)       

def printgay(n):
    gay=1
    for i in range(n, -2):
        print("ggay")
# printgay(-1)

def recur(n):
    if (n == 0):
        return
    else:
        print("recursion")
        recur(n)


def calculateSum(n):
    if (n == 0):
        return 0
                                  
    return calculateSum(n-1) +  n
    
print(calculateSum(5))
#  5 4 3 2 1 0 


'''
P6-4 Exercise: Palindrome Word (Revisited)
A phrase is a palindrome if it reads the same forward and backward.

For example, the word "radar" is a palindrome since the spelling is the same if we flip the words forward to backward. The word "backpack" is not a palindrome since it spells "kcapkcab" backwards, which is not the same as the original word.

Problem Statement
Write a function that checks whether a string is a palindrome or not. The function should take in a string as a parameter, and return True if it is a palindrome, or False otherwise.

Try to solve this problem using recursion.

What is the base case for this program? Is there one, two, or more cases?
What is the general case?
Example 1:

'''       

word = "level"

'''
A phrase is a palindrome if it reads the same forward and backward.

For example, the word "radar" is a palindrome since the spelling is the same if we flip the words forward to backward. The word "backpack" is not a palindrome since it spells "kcapkcab" backwards, which is not the same as the original word.
'''
# https://www.youtube.com/watch?v=ngCos392W4w
# output: True
def gay(n):
    ({})