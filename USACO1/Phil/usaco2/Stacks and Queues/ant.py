p = "{()}[]"
gay=[]
def val():
    for i in p:
        if i == '[' or i == '(' or i =='{':
            gay.append(i)
            print(gay)
        if len(gay)>0:
            if i == ']' and gay[-1] == '[':
                gay.pop()
            elif i == '}' and gay[-1] == '{':
                gay.pop()
            elif i == ')' and gay[-1] == '(':
                gay.pop()
    if gay == []:
        return True
    else:
        print("no")
val()

            