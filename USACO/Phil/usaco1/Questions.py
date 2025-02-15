'''
Problem 1
Given a list of strings and a string variable target, write a program that checks whether the string variable target exists inside the list.

python
names = ['Eve', 'Alice', 'Bob', 'Ivan', 'Gary', 'Claudia', 'Brooks', 'Lappland']
target = 'Gary'
'''
# names = ['Eve', 'Alice', 'Bob', 'Ivan', 'Gary', 'Claudia', 'Brooks', 'Lappland']
# target = 'Gary'
# x=0
# for gay in names:
#     if target in gay:
#         print("ture,",x)
#     x+=1

# if target in names:
#     print(names.index(target))

nums1 = [3, 5, 19]
nums2 = [0, 1, 4]
count1 = len(nums1)
count2 = len(nums2)
yeegay=[]
i , j = 0
while i < count1 and j < count2:
    if nums1[i]< nums2[j]:
        yeegay.append(j)
        i +=1
    if nums2[j]<nums1[i]:
        yeegay.append(i)
        j+=1
    if nums2[j]==nums1[i]:
        yeegay.append(i,j)
        j+=1
        i+=1

