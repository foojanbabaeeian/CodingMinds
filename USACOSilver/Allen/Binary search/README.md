# https://usaco.org/index.php?page=viewproblem2&cpid=714

'''
Farmer John's cows are trying to learn to cross the road effectively. Remembering the old "why did the chicken cross the road?" joke, they figure the chickens must be experts on crossing the road, and go off in search of chickens to help them.
As it turns out, chickens are very busy creatures and have limited time to help the cows. There are C
chickens on the farm (1≤C≤20,000
), conveniently numbered 1…C
, and each chicken i
is only willing to help a cow at precisely time Ti
. The cows, never in a hurry, have more flexibility in their schedules. There are N
cows on the farm (1≤N≤20,000
), conveniently numbered 1…N
, where cow j
is able to cross the road between time Aj
and time Bj
. Figuring the "buddy system" is the best way to proceed, each cow j
would ideally like to find a chicken i
to help her cross the road; in order for their schedules to be compatible, i
and j
must satisfy Aj≤Ti≤Bj
.

If each cow can be paired with at most one chicken and each chicken with at most one cow, please help compute the maximum number of cow-chicken pairs that can be constructed.

INPUT FORMAT (file helpcross.in):
The first line of input contains C
and N
. The next C
lines contain T1…TC
, and the next N
lines contain Aj
and Bj
(Aj≤Bj
) for j=1…N
. The A
's, B
's, and T
's are all non-negative integers (not necessarily distinct) of size at most 1,000,000,000.
OUTPUT FORMAT (file helpcross.out):
Please compute the maximum possible number of cow-chicken pairs.
SAMPLE INPUT:
5 4
7
8
6
2
9
2 5
4 9
0 3
8 13
SAMPLE OUTPUT:
3
'''

Homework:

This is the github page where you can find the problems and answer we work on in class:
https://github.com/foojanbabaeeian/CodingMinds

Here is the google drive I told you about:
https://drive.google.com/drive/folders/18nfNBBP-h4hgUJxX1hB2DFE7DPMZ2OJ9?usp=sharing

Your homework is reading more about binary search:
Binary Search
Binary Search Fundamentals
A complete explanation about binary search can be found at: https://www.geeksforgeeks.org/binary-search/

Recursive
Non-recursive (preferred)
java
// binary search
public static int binarySearch(int[] nums, int target) {
int left = 0;
int right = nums.length - 1;

    while(left <= right) {
      int middle = left + (right - left) / 2;
      if (nums[middle] == target) {
        return middle;
      }
      if (nums[middle] > target) {
        right = middle - 1;
      }
      if (nums[middle] < target) {
        left = middle + 1;
      }
    }

    return -1;

}
Variants of Binary Search
Based on the standard binary search version shown above, could you please try to solve the following version of the binary search (please see the link below for the complete description of each variant):

Index of first occurrence of a key
Index of last occurrence of a key
Index of least element greater than key
Index of greatest element less than key
Please see the reference here and make sure that you understand all these variants: https://www.geeksforgeeks.org/variants-of-binary-search/

Lecture Video
Youtube Lecture Link: https://www.youtube.com/watch?v=H1Jo-WzHTIc


https://usaco.org/index.php?page=viewproblem2&cpid=858
