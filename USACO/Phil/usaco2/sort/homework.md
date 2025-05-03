# L8 Assessment - Sorting Algorithms

## Bubble Sort

[Bubble Sort](https://www.geeksforgeeks.org/bubble-sort-algorithm/)
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity are quite high.

We sort the array using multiple passes. After the first pass, the maximum element goes to end (its correct position). Same way, after second pass, the second largest element goes to second last position and so on.
In every pass, we process only those elements that have already not moved to correct position. After k passes, the largest k elements must have been moved to the last k positions.
In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.


## Selection Sort


[Selection Sort](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)
Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.

## Insertion Sort

[Insertion Sort](https://www.geeksforgeeks.org/insertion-sort-algorithm/)
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

We start with the second element of the array as the first element is assumed to be sorted.
Compare the second element with the first element if the second element is smaller then swap them.
Move to the third element, compare it with the first two elements, and put it in its correct position
Repeat until the entire array is sorted.


## Merge Sort 
[Merge Sort](https://www.geeksforgeeks.org/merge-sort/)

How does Merge Sort work?
Here’s a step-by-step explanation of how merge sort works:

Divide:  Divide the list or array recursively into two halves until it can no more be divided. 
Conquer:  Each subarray is sorted individually using the merge sort algorithm. 
Merge:  The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged. 

## Quick Sort

[Quick Sort](https://www.geeksforgeeks.org/quick-sort-algorithm/)

QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

There are mainly three steps in the algorithm:

Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.



## Problem 1

What are some common sorting algorithms? Explain the pseudo code for one of them.

## Problem 2

What is the basic idea of merge sort/quick sort?

## Problem 3

What is the time complexity of merge sort/quick sort?

## Problem 4

If a program were to have a merge sort sorting function in it, such as the one below, what is the overall time complexity of the program?

```python
nums = [10, 9, 1, 10, 6, 0, 1, 1, 8, 5]

nums.sort()
for i in range(len(nums)):
    print(nums[i])
```