# # def gay(x,n):
# #     if x**2==n:
# #         print("True")
# #         return
# #     elif x>n/2:
# #         print("False")
# #         return
# #     else:
# #         x+=1
# #         gay(x,n)
# # gay(1,9)
# def fizz(x,y):
#     if x%3 ==0:
#         if x%5 ==0:
#             print("Fizz Buzz")
#             x+=1
#             if x==y:
#                 print("Fizz Buzz")
#                 return
#             fizz(x,y)
#         else:
#             print("Fizz")
#             x+=1
#             if x==y:
#                 print("Fizz")
#                 return
#             fizz(x,y)
#     elif x%5 ==0:
#         print("Buzz")
#         x+=1
#         if x==y:
#             print("Buzz")
#             return
#         fizz(x,y)
#     else:
#         print(x)
#         x+=1
#         if x==y:
#             print(x)
#             return
#         fizz(x,y)
# fizz(1,50)
import time
start=time.time()
# dict = {}
# tcid = {}
# def gay(s1,s2):
#     if len(s1)==len(s2):
#         for i in s1:
#             if i in dict:
#                 dict[i]+=1
#             else:
#                 dict[i]=1
#         for i in s2:
#             if i in tcid:
#                 tcid[i]+=1
#             else:
#                 tcid[i]=1
#         for i in dict:
#             if i in tcid:
#                 if dict[i] != tcid[i]:
#                     return False                    
#                 else:
#                     pass
#         return True
# print(gay("noob","boon"))
boo =[1,79,2,8,4]
boo.sort()
product = 1
start = -1
for i in range(3):
    product *= boo[start] 
    start -= 1
print(time.time()-start)
