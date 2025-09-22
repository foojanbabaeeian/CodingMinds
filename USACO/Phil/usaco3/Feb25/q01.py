'''
USACO 2025 February Contest, Bronze
Problem 1. Reflection
Farmer John has a square canvas represented by an N by N grid of cells (2≤N≤2000, N is even). He paints the canvas according to the following steps:

First, he divides the canvas into four equal quadrants, separated by horizontal and vertical lines through the center of the canvas.
Next, he paints a lovely painting in the top-right quadrant of the canvas. Each cell of the top-right quadrant will either be painted (represented by '#') or unpainted (represented by '.').
Finally, since he is so proud of his painting, he reflects it across the previously mentioned horizontal and vertical lines into the other quadrants of the canvas.
For example, suppose N=8 and FJ painted the following painting in the top-right quadrant in step 2:

.#..
.#..
.##.
....
Then after reflecting across the horizontal and vertical lines into the other quadrants in step 3, the canvas would look as follows:

..#..#..
..#..#..
.##..##.
........
........
.##..##.
..#..#..
..#..#..
However, while FJ was sleeping, Bessie broke into his barn and stole his precious canvas. She totally vandalized the canvas—removing some painted cells and adding more painted cells! Before FJ woke up, she returned the canvas to FJ.

FJ would like to modify his canvas so that it once again satisfies the reflective condition: that is, it is the result of reflecting the top-right quadrant into each of the other quadrants. Since he only has a limited number of resources, he would like to achieve this in as few operations as possible, where a single operation consists of either painting a cell or removing paint from a cell.

You are given the canvas after Bessie's vandalism, as well as a sequence of U (0≤U≤105) updates to the canvas, each toggling a single cell to '.' if it is '#', or vice versa. Before any updates, and after each update, output the minimum number of operations x FJ needs to perform so that the reflective condition is satisfied.

INPUT FORMAT (input arrives from the terminal / stdin):
The first line contains integers N and U
.
The next N lines each contain N characters representing the canvas after Bessie's vandalism. Every character is either '#' or '.'.

The following U lines each contain integers r and c , where 1≤r,c≤N , representing an update to the cell in the rth row from the top and c th column from the left of the canvas.

OUTPUT FORMAT (print output to the terminal / stdout):
Output U+1 lines representing x before any updates and after each update.
SAMPLE INPUT:
4 5
..#.
##.#
####
..##

1 3

2 3

4 3

4 4

4 4

....
####
####
....

SAMPLE OUTPUT:
4
3
2
1
0
1
The following canvas satisfies the reflective condition and differs from the original canvas by 4 operations:

....
####
####
....
It is impossible to make the original canvas satisfy the reflective condition using fewer than 4 operations.

After updating (1,3)
, the canvas looks like this:

....
##.#
####
..##
It now takes 3 operations to make the canvas satisfy the reflective condition.

After updating (2,3)
, the canvas looks like this:

....
####
####
..##
It now takes 2 operations to make the canvas satisfy the reflective condition.

SCORING:
Inputs 2-3: N≤4
Inputs 4-6: U≤10
Inputs 7-16: No additional constraints.
Problem credits: Chongtian Ma

Contest has ended. No further submissions allowed.

'''
gay = input()