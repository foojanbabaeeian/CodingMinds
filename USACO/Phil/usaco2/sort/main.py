# You have a list of integers, you want to sort them in non-decreasing order.

'''
# How do add an element to a list at a specific index?
list = [1, 3, 4, 5]
list.insert(1, 2)
# insert (index, element) method inserts the element at the specified index.
# [1, 200, 3, 4, 5]
print(list)
'''

nums = [1,2, 5, 7, 8, 3, 6, 8, 3]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
         for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
            
# bubble_sort(nums)

'''
Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.

选择排序是一种基于比较的排序算法。它通过反复从未排序部分中选择最小（或最大）元素并将其与第一个未排序元素交换来对数组进行排序。此过程持续进行，直到整个数组排序完毕。

首先，我们找到最小的元素，并将其与第一个元素交换。这样，我们就得到了位于正确位置的最小元素。
然后我们在剩余元素中找到最小的（或第二小的）并将其与第二个元素交换。
我们继续这样做，直到所有元素都移动到正确的位置。
'''

def selection_sort(nums):