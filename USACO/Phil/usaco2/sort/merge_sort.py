'''
P9-4 Exercise: Merge Two Sorted Lists
Problem Satement
Given two sorted lists, write a function that merge these two sorted list into one single large sorted list and return the result.

You cannot use the sort() function in your solution.

Example 1:

python
nums1 = [3, 5, 19]
nums2 = [0, 1, 4]

# output: [0, 1, 3, 4, 5, 19]
print(mergeLists(nums1, nums2))
Example 2:

python
nums1 = [1, 7]
nums2 = [3, 5, 6]

# output: [1, 3, 5, 6, 7]
print(mergeLists(nums1, nums2))
'''


nums1 = [1, 7]
nums2 = [3, 5, 6, 9, 10, 11, 12, 13, 14, 15]
nums3=[]
x=0
y=0
while x < len(nums1) and y < len(nums2):
        
    if nums1[x]<=nums2[y]:
        nums3.append(nums1[x])
        
        x+=1
    else:
        nums3.append(nums2[y])
    
        y+=1

while y == len(nums2) and x !=len(nums1):
    nums3.append(nums1[x])
    x+=1


while x == len(nums1) and y !=len(nums2):
    nums3.append(nums2[y])
    y+=1


print(nums3)
# output: [0, 1, 3, 4, 5, 19]

