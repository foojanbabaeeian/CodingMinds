Practice Question 3: Array Partition
Problem Statement
Leetcode: Array Partition

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:

python
nums = [1, 4, 3, 2]

# output: 4
# explanation:
# Below are all possible pairings (ignoring the ordering of the elements)
#   1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
#   1. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
#   1. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# Hence the maximum possible sum is 4.
print(arrPartition(nums))
Example 2:

python
nums = [6, 2, 6, 5, 1, 2]

# output: 9
# explanation:
#   The optimal pairing is (2, 1), (2, 5), (6, 6), which gives
#   us: min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9
print(arrPartition(nums))