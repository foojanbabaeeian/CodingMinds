# sorting the list of cows' arrivals 
# search and find the max 
# The lower bound => 0
# The upper bound => differnce between the earliest and the latest arrival times


def cows(arrivals, M, C, W):
    bus = 1
    first_cow = arrivals[0]
    cow_in_bus = 0
    for cow in arrivals: 
        if cow_in_bus < C and cow - first_cow <= W:
            cow_in_bus += 1
        else: 
            bus +=1
            cow_in_bus = 1
            first_cow= cow

        if bus > M:
            return False
        
    return True

def min_max_waiting(N, M, C, arrivals):
    arrivals.sort()
    low = 0
    high = max(arrivals) - min(arrivals)
    while low < high:
        mid = (high + low) //2
        if cows(arrivals, M, C, mid):
            high = mid
        else:
            low = mid + 1
    return low

with open("convention.in", "r") as fin:
    N, M, C = map(int, fin.readline().strip().split())
    arrivals= list(map(int, fin.readline().strip().split()))
ans = min_max_waiting(N, M, C, arrivals)

with open("convention.out", "w") as fout:
    fout.write(f"{ans}\n")