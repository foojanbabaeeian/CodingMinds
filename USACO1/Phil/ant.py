# def gay(x,n):
#     if x**2==n:
#         print("True")
#         return
#     elif x>n/2:
#         print("False")
#         return
#     else:
#         x+=1
#         gay(x,n)
# gay(1,9)
def fizz(x,y):
    if type(x/3)== int:
        if type(x/5)== int:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif type(x/5)== int:
        print("Buzz")
    else:
        print(x)
        x+=1
        if x==50:
            print(x)
            return
fizz(1,50)