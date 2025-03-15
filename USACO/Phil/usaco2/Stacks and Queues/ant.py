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
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
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
            else:
                gays.append(i)
        if gay == gays:
            return True
        else:
            return False