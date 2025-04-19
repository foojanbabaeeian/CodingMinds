gay = [1,4,3,2]
gay.sort()
sum=0
for i in range(0,len(gay),2):
    sum += gay[i]

print(sum)