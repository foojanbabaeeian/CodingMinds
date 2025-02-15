# https://usaco.org/index.php?page=viewproblem2&cpid=57

'''
SAMPLE INPUT:
6 3
2
1
1
3
2
1
1 6
3 3
2 4
SAMPLE OUTPUT:
3 2 1
1 0 0
2 0 1
'''

N, Q = map(int, input().split())
breeds = [0] * (N + 1) 

for i in range(1, N + 1):
    breeds[i] = int(input().strip())

holsteins = [0] * (N + 1)
guernseys = [0] * (N + 1)
jerseys = [0] * (N + 1)

for i in range(1, N + 1):
    holsteins[i] = holsteins[i - 1] + (1 if breeds[i] == 1 else 0)
    guernseys[i] = guernseys[i - 1] + (1 if breeds[i] == 2 else 0)
    jerseys[i] = jerseys[i - 1] + (1 if breeds[i] == 3 else 0)

result = []
for _ in range(Q):
    a, b = map(int, input().split())
    h_count = holsteins[b] - holsteins[a - 1]
    g_count = guernseys[b] - guernseys[a - 1]
    j_count = jerseys[b] - jerseys[a - 1]
    result.append(f"{h_count} {g_count} {j_count}")

print("\n".join(result) + "\n")