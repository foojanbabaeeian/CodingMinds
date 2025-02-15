# Practice Question 2: Maximum 69 Number

## Problem Statement

## Leetcode: Maximum 69 Number

### Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, or 9 becomes 6)

Example 1:

python
num = 9669

# output: 9969

# explanation:

# changing the first digit results in 6669.

# changing the second digit results in 9969.

# changing the third digit results in 9699.

# changing the fourth digit results in 9666.

print(max69Number(num))
Example 2:

python
num = 9996

# output: 9999

print(max69Number(num))
Example 3:

python
num = 9999

# output: 9999

# explanation: It is better to not apply any changes

print(max69Number(num))
