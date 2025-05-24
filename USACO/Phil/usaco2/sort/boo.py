'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

height = [1,8,6,2,5,4,8,3,7]

# def maxArea(height):
#     max_area = 0
#     for gay in range(len(height)): 
#         for les in range(gay+1, len(height)):
#             x = min(height[gay], height[les])
#             area = x * abs(gay-les)
#             if max_area < area:
#                 max_area = area
#     return max_area

# print(maxArea(height))  


def maxArea(height):
    start = 0
    end = len(height) - 1
    max_area = 0
    while start < end:
        distance = end - start
        min_height = min(height[start], height[end])
        area = distance * min_height
        if area > max_area:
            max_area = area
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1


'''
392. Is Subsequence
Easy
Topics
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''