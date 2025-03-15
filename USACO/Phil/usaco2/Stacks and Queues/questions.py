'''
L5-1 What is a Stack
Stack Methods
Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Note that an empty string is also considered valid.

Example 1:

python
p = "()[]{}"

# output: True
print(validParenthesis(p))
Example 2:

python
p = "{()}[]"

# output: True
print(validParenthesis(p))
Example 3:

python
p = "[}"

# output: False
print(validParenthesis(p))
'''


'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''