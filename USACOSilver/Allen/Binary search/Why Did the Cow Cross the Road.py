
C, N = map(int, input().split())
chickens = []
for i in range(C):
    T = int(input())
    chickens.append(T)
cows = []
for i in range(N):
    Aj  , Bj = map(int, input().split())
    cows.append((Aj, Bj))

chickens.sort()
cows.sort()

count = 0
check = []
cow_num = 0
for chicken in chickens:
    while cow_num < N and cows[cow_num][0] <= chicken:
        pass

'''
# Examples

# Chicken :
[7, 8, 6, 2, 9]
# Cows:
[
    (2,5),
    (4,9),
    (0,3), 
    (8,13)
]

# sort 
[2, 6,7, 8, 9]

[
    (0,3), #1
    (2,5), #2
    (4,9), #3
    (8,13) #4
]
'''