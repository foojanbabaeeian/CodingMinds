'''
Practice Question 11: Maximum Product of Three Numbers
Given a list of positive integers with a length greater than 3, find three numbers whose product and is maximum and output the maximum product.

Example 1:

python
nums = [1, 6, 5, 2, 10]

# output: 300
# This is because 6 * 5 * 10 = 300
print(maxProduct(nums))
'''

def maxProduct(nums):
    nums.sort()
    return nums[-1] * nums[-2] * nums[-3]