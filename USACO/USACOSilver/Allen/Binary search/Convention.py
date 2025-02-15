# https://usaco.org/index.php?page=viewproblem2&cpid=858

def can_assign(wait, N, M, C, t):
    buses = 1  # Start with the first bus
    first_cow = t[0]  # Arrival time of the first cow in the current bus
    count = 0  # Number of cows in the current bus

    for i in range(N):
        # If adding the current cow exceeds the waiting time or bus capacity, start a new bus
        if t[i] - first_cow > wait or count == C:
            buses += 1
            first_cow = t[i]
            count = 1  # Current cow starts the new bus
        else:
            count += 1

    return buses <= M  # Check if the total buses used is within the limit


def main():
    # File handling for USACO submission
    with open("convention.in", "r") as fin:
        data = fin.read().split()

    # Parse input
    N, M, C = map(int, data[:3])
    t = list(map(int, data[3:]))

    # Sort arrival times
    t.sort()

    # Binary search for the minimum maximum waiting time
    low, high = 0, t[-1] - t[0]  # Possible range of waiting times
    while low < high:
        mid = (low + high) // 2
        if can_assign(mid, N, M, C, t):
            high = mid  # Try a smaller waiting time
        else:
            low = mid + 1  # Increase the waiting time

    # Write output to the file
    with open("convention.out", "w") as fout:
        fout.write(f"{low}\n")

