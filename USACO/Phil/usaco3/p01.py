# https://usaco.org/index.php?page=viewproblem2&cpid=785
start = 0
x =0
y=0
cow=[1,2,3,5,6,7,4,7,8]
for i in range(len(cow)):
    x+=1
    if cow[i] <= cow[x]:
        pass
    else:
        y = cow[x]
        break
for i in range(len(cow)):
    if cow[i] <= y:
        pass
    else:
        start = i 
        break


distance = x - start
new_cow = cow[start:x]
print(x, start, distance, new_cow)
