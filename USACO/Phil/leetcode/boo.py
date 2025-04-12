def problem1():
    num="IIL"
    sv ={ "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def roman():
        number = 0
        for i in range(len(num)-1):
            if sv[num[i]] < sv[num[i+1]]:
                number -= sv[num[i]]
            else:  
                number += sv[num[i]]
        return number
    roman()

'''
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

'''
# https://leetcode.com/problems/maximum-69-number/description/
num = 9699
numL = list(str(num))

# output: 9969

# explanation:

# changing the first digit results in 6669.

# changing the second digit results in 9969.

# changing the third digit results in 9699.

# changing the fourth digit results in 9666.


def max69Number(numL):
    x=0
    ans=""
    for i in numL:
        if x <= len(numL):
            if i =='6':
                numL[x] = '9'
            for i in numL:
                ans += i
                return int(ans)
        else:
            print("no bigger possible")
        x+=1
    for i in numL:
        ans += i
    return int(ans)



print(max69Number(numL))


class Solution:
    def maximum69Number (self, num: int) -> int:
        x=0
        ans=""
        numL = list(str(num))

        for i in numL:
            if x <= len(numL):
                if i =='6':
                    numL[x] = '9'
                    for i in numL:
                        ans += i
                    return int(ans)
            x+=1
        for i in numL:
            ans += i
        return int(ans)