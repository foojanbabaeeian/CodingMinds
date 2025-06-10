'''
P3-3 Exercise: Find the Element that Appeared the Most Times
Problem Statement
Given an integer list nums, write a function that finds the number that has appeared the highest number of times in the list. Assume the list always has one answer.

Can you solve it in a linear time complexity O(n)? Hint: Use a dictionary instead of nested loops.

Example 1:


nums = [3, 1, 1, 2, 1, 1, 3, 2, 2, 3]

# output: 1
print(mostCommon(nums))
Example 2:


nums = [3, 2, 3]

# output: 3
print(mostCommon(nums))
'''

def mostCommon_N2(nums):
    '''
    -> List of ints 
    
    Return the number that appeared the most in the list
    '''
    # Go through the list nums with a for loop 
    # we see if the index in the loop is equal to any of the indexes after it 
        # For wex we are going to use [:] indexing and if there is we continue but then if it isn't we will remove it from the list
    # We continue doing that until we have gone through all the numbers
    '''

    1. iterate through the list -> we store the number we are on in a variable 
        [1, 2, 3, 4] we start with var = 1
    2. iterate through the list again to see if any of the items now equal to the element that we are checking them with ->. we count up how many time the element has appeared in the list
        1 == 2: they are equal and then check 3, 4 and the rest of the list 
    3. store the element that appeared the most amount of times in the max
    4. if the amount of time that the element appeared in the list was more than the max that we already have we are going to replace it 
        else we are going to move on 

    return the number that is saved in the max var
    '''
    max = 0
    max_num = 0

    for num in nums:
        current = num

        count = 0
        for check in nums:
            if num == check:
                count += 1

        if count > max:
            max = count
            max_num = current 
    return max_num
                
        

# nums = [3, 1, 1, 2, 1, 1, 3, 2, 2, 3]

# # output: 1
# print(mostCommon(nums))

# # Why use dictionaries? 
    # easier because we can store the key and the value. instead of variables that represent the key or the value
'''
do a for loop and do counts 
create a dictionary and then we store the key[and then teh count of it]
we go over and store the keys 

count and return 

create a new dictioanry -> include the keys which are the numbers and the values which are the count 
'''
def mostCommon(nums):
    count_dic = {}
    for i in nums:
        count_dic[i] = 