# # # def gay(x,n):
# # #     if x**2==n:
# # #         print("True")
# # #         return
# # #     elif x>n/2:
# # #         print("False")
# # #         return
# # #     else:
# # #         x+=1
# # #         gay(x,n)
# # # gay(1,9)
# # def fizz(x,y):
# #     if x%3 ==0:
# #         if x%5 ==0:
# #             print("Fizz Buzz")
# #             x+=1
# #             if x==y:
# #                 print("Fizz Buzz")
# #                 return
# #             fizz(x,y)
# #         else:
# #             print("Fizz")
# #             x+=1
# #             if x==y:
# #                 print("Fizz")
# #                 return
# #             fizz(x,y)
# #     elif x%5 ==0:
# #         print("Buzz")
# #         x+=1
# #         if x==y:
# #             print("Buzz")
# #             return
# #         fizz(x,y)
# #     else:
# #         print(x)
# #         x+=1
# #         if x==y:
# #             print(x)
# #             return
# #         fizz(x,y)
# # fizz(1,50)
# import time
# start=time.time()
# # dict = {}
# # tcid = {}
# # def gay(s1,s2):
# #     if len(s1)==len(s2):
# #         for i in s1:
# #             if i in dict:
# #                 dict[i]+=1
# #             else:
# #                 dict[i]=1
# #         for i in s2:
# #             if i in tcid:
# #                 tcid[i]+=1
# #             else:
# #                 tcid[i]=1
# #         for i in dict:
# #             if i in tcid:
# #                 if dict[i] != tcid[i]:
# #                     return False                    
# #                 else:
# #                     pass
# #         return True
# # print(gay("noob","boon"))
# boo =[1,79,2,8,4]
# boo.sort()
# product = 1
# start = -1
# for i in range(3):
#     product *= boo[start] 
#     start -= 1
import time
start=time.time()
# n=1000
# x=n-1
# y=n*x
# for i in range(n-2):
#     x+=-1
#     y = y*x
# print(y)
# gay = ["james","gayy","gayyyyyyy","noob","gayyy"]
# bis = 0
# for gays in gay:
#     x =len(gays)
#     if x > bis:
#         bis = x
# print(bis)
# for gays in gay:
#     x =len(gays)
#     if x==bis:
#         print(gays)
# gpa =[1,2,3,4,5,6]
# gpa.sort
# x=0 
# for gay in gpa:
#     x=x+gay
# print(x/len(gpa))
# print(time.time()-start)
# import math
# gpa =[3.5,2.5,3.7,3.14,3.42]
# gpa.sort()
# z=3*((len(gpa)+1)/4)
# print(round(z))
# print(gpa[int(z-1)])
'''
Practice Question 17: Maximum of Three Numbers
Write a function that finds the maximum of the three numbers. Try not to use Python's built in functions such as sort().

Example 1:

python
# output: 15
print(max(3, 15, 9))
Example 2:

python
# output: 0
print(max(-1, -4, 0))

Practice Question 18: Rounding Numbers
Write a function that rounds a number to the 2nd place. Try not to use Python's built in functions such as round().

Example 1:

python
# output: 3.14
print(roundNum(3.1415926))
Example 2:

python
# output: 2.72
print(roundNum(2.718281828))'''
# gays = [0,90,1]
# x=0
# for gay in gays:
#     if gay < x: 
#         pass
#     else:
#         x=gay
# print(x)
'''
Rounding Numbers
Write a function that rounds a number to the 2nd place. Try not to use Python's built in functions such as round().

Example 1:

python
# output: 3.14
print(roundNum(3.1415926))
Example 2:

python
# output: 2.72
print(roundNum(2.718281828))'''
gay = 3.1475926
gaystr = str(gay)
if int(gaystr[4])>4:
    gaystr = float(gaystr[:4])+0.01
    print(gaystr)
else:
    print(gaystr[:4])
print(time.time()-start)
#