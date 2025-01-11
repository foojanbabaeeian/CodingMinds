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
gpa =[1,2,3,4,5,6]
gpa.sort
x=0
for gay in gpa:
    x=x+gay
print(x/len(gpa))
print(time.time()-start)