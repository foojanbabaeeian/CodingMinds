# Practice Question 16: Count Non Unique Numbers
# Count how many numbers that has appeared two or more times in a given list.

# Example 1:

# python
# nums = [8, 1, 10, 1, 2, 2, 8, 7, 10, 3]

# # output: 4
# # number 1, 2, 8, and 10 has appeared two or more times
# print(countNonUnique(nums))
# Example 2:

# python
# nums = [2, 5, 10, 7, 6, 2, 7, 5, 10, 2, 6, 10]

# # output: 5
# # number 2, 5, 6, 7, and 10 has appeared two or more times
# print(countNonUnique(nums))
nums = [2, 5, 10, 7, 6, 2, 7, 5, 10, 2, 6, 10]
gay=[]
gayy=0
for num in nums:
    if num in gay:
        pass
    else:
        if nums.count(num)>= 1:
            gayy+=1
            gay.append(num)
        else:
            pass
print(gayy)