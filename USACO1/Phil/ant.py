def gay(x,n):
    if x**2==n:
        print("True")
        return
    elif x>n/2:
        print("False")
        return
    else:
        x+=1
        gay(x,n)
gay(1,9)