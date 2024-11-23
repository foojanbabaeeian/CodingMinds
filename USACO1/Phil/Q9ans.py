import time 
start = time.time()
def fizz(num):
    if num % 15 == 0:
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
n = 1
number = 100000
while n<= number:
    fizz(n)
    n +=1 
print(time.time() - start)