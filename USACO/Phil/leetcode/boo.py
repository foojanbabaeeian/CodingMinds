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
def problem2():



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
        




'''
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
'''

