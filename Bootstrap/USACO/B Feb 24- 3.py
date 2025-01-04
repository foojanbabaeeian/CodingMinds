N, Q = (int(x) for x in input().split())
c = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
diffs = sorted([ci - ti for ci, ti in zip(c, t)], reverse=True)
for _ in range(Q):
    V, S = (int(x) for x in input().split())
    print("YES" if (V <= N and (V <= 0 or diffs[V-1] > S)) else "NO")