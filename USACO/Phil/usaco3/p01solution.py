'''
农夫约翰雄心勃勃，计划尝试一件似乎总是不太顺利的事情：他想给他的整个牛群拍照。
为了让照片看起来更美观，他希望奶牛从最矮到最高排成一排。不幸的是，就在他让奶牛这样排好队后，总是爱惹麻烦的贝西奶牛走出了队伍，重新排到了队伍的其他位置！

农夫约翰想要交换几对奶牛，以便整个牛群再次正确排列。请帮助他确定实现此目标所需的最少交换次数。

输入格式（文件 outofplace.in）：
输入的第一行包含否
（2≤N​​≤ 100
）下一个否
线描述了 Bessie 移动后奶牛排成一排时的高度。每头奶牛的高度都是一个整数，范围是1 … 1,000,000​​​​
。奶牛可能身高相同。
输出格式（文件 outofplace.out）：
请输出 Farmer John 需要交换奶牛的最少次数，才能达到正确的排序。交换不一定需要涉及相邻奶牛的排序。
样本输入：
6 
2 
4 
7 
7 
9 
3
样本输出：
3
在这个例子中，Bessie 显然是高度为 3 的奶牛。FJ 使用如下所述的三次交换将奶牛恢复到排序顺序：

2 4 7 7 9 3 - 原始阵容
2 4 7 7 3 9 - 交换最后两头牛
2 4 3 7 7 9 - 交换第一个 7 和 3 
2 3 4 7 7 9 - 交换 4 和 3
'''

'''
Farmer John would like to swap pairs of cows so the entire herd is again lined up properly. Please help him determine the minimum number of swaps he needs to make between pairs of cows in order to achieve this goal.

INPUT FORMAT (file outofplace.in):
The first line of input contains N
 (2≤N≤100
). The next N
 lines describe the heights of the cows as they are lined up after Bessie makes her move. Each cow height is an integer in the range 1…1,000,000
. Cows may have the same height.
OUTPUT FORMAT (file outofplace.out):
Please output the minimum number of times Farmer John needs to swap pairs of cows in order to achieve a proper ordering. Swaps do not necessarily need to involve adjacent cows in the ordering.
SAMPLE INPUT:
6
2
4
7
7
9
3
SAMPLE OUTPUT:
3
In this example, Bessie is clearly the cow of height 3. FJ return the cows to sorted order using three swaps as described below:

2 4 7 7 9 3 - Original Lineup
2 4 7 7 3 9 - Swap the last two cows
2 4 3 7 7 9 - Swap the first 7 and 3
2 3 4 7 7 9 - Swap 4 and 3

'''
# Take the input
# loop through the list
#   1. Compare them
#   [ 2 4 7 7 9 3 ]

#   var = 0
#  var2 = 0 

