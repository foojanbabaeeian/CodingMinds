num="IIL"
sv ={ "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def roman():
    number = 0
    for i in range(len(num)-1):
        if sv[num[i]] < sv[num[i+1]]:
            number -= sv[num[i]]
        else:  
            number += sv[num[i]]
    return number
roman()