'''Practice Question 7: Fibonacci Number
Write a program to find the Nth number in a Fibonacci sequence. 
In a Fibonacci sequence, we start with the numbers 0 and 1 as our first two numbers. We define the ith number as the sum of i - 1th number and i - 2th number.

Example:

python
n = 10

# output: 34
# The Fibonacci sequence up until the 10-th element is the following:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
printFibonacci(n)'''
n=6
x=0
y=1
for i in range(n-1):
    x, y = y, x + y
    # chatgpt give me a way called tuple unpacking
print(x)