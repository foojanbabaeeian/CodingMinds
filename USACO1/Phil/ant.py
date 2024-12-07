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
s1 ="noob"
s2 ="boon"
dict = {}
tcid = {}
if len(s1)==len(s2):
    for i in s1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in s2:
        if i in tcid:
            tcid[i]+=1
        else:
            tcid[i]=1
    for i in dict:
        if i == tcid[i]:
            print("ture")

