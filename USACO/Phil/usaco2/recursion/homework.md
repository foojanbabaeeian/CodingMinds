## L6 Assessment - Recursion
### Problem 1

Use your own words, explain what is recursion.

### Problem 2

Convert the following code from a recursive function into a loop.
```bash 
python
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n * factorial(n - 1)
```

### Problem 3

Convert the following code from a recursive function into a loop.
```bash
python
def printElement(n):
    if (n == 0):
        return
    else:
        print("Hi there")
        printElement(n - 1)
```

### Problem 4

What is the problem with the following code?
```bash 
python
def recur(n):
    if (n == 0):
        return
    else:
        print("recursion")
        recur(n)

```

### Problem 5

What is the problem with the following code?
```bash 
python
def calculateSum(n):
    if (n == 0):
        return 0
    else:
        return calculateSum(n) + n
```
### Problem 6

The fibonacci numbers are the numbers in the following sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Where the first two numbers are 0 and 1, with each subsequent number defined as the sum of the previous two numbers in the sequence.

Write a function that calculates the nth number in the sequence using recursion.