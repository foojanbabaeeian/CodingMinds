# Please complete Practice Question 8: Valid Perfect Square: A perfect square is when there is an integer x whose squared value is equal to n.
#  Given a positive integer n, write a function that returns True if n is a perfect square. Return False otherwise.
# Do not use any built-in library function such as sqrt.
n = 99
x = 0
def gay(x,n):
    while x/2==n:
        print("False")
        break
    while x**2==n:
        print("Ture")
        break
    else:
        x+=1
        gay(x,n)
gay(x,n)