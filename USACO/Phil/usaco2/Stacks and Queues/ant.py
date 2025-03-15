# p = "{()}[]"
# gay=[]
# def val():
#     for i in p:
#         if i == '[' or i == '(' or i =='{':
#             gay.append(i)
#             print(gay)
#         if len(gay)>0:
#             if i == ']' and gay[-1] == '[':
#                 gay.pop()
#             elif i == '}' and gay[-1] == '{':
#                 gay.pop()
#             elif i == ')' and gay[-1] == '(':
#                 gay.pop()
#     if gay == []:
#         return True
#     else:
#         print("no")
# val()
s = "y#f#o##f"
t = "y#fo##f"
gay = []
gays =[]
for i in s:
    if i == "#":
        if len(gay) != 0:
            gay.pop()
        else:
            pass
    else:
        gay.append(i)
for i in t:
    if i == "#":
        if len(gays) != 0:
            gays.pop()
        else:
            pass
            gays.pop()
    else:
        gays.append(i)
if gay == gays:
    print("true")
else:
    print("false")