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