'''
Write a function named max, that returns the greater number of two given numbers a and b.

'''

def max(a,b):
    return a if a>b else b


# or another way to do it is

def max(a,b):
    if a > b:
        return a
    else:
        return b

print(max(3,4))