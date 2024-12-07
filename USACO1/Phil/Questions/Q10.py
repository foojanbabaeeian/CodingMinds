'''
Practice Question 10: Valid Anagram
An anagram is a word formed by rearranging the letters of a different word. Given two strings s1 and s2, return True if s1 is an anagram of s2. Return false otherwise.

Example 1:

python
s1 = "listen"
s2 = "silent"

# output: True
print(isAnagram(s1, s2))
'''

s1 ="noob"
s2 ="boon"

# def create_dict(word):
#     dictionary = {}
#     for i in word:
#         if i in dictionary:
#             dictionary[i] += 1
#         else:
#             dictionary[i] = 1
#     return dictionary
# dict1  = create_dict(s1)

# dict2  = create_dict(s2)
# def isanagram(dict1, dict2):
#     for k in dict1:
#         if dict2[k] != dict1[k]:
#             return False
#     return True
import time
start = time.time()

def isanagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else: 
        return False

print(isanagram(s1,s2))
print(time.time() - start)