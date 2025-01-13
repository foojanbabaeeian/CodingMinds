def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, F = int(data[0]), int(data[1])
    input_str = data[2]
    
    # Initialize frequency and max frequency matrices
    freq = [[0] * 26 for _ in range(26)]
    maxfreq = [[0] * 26 for _ in range(26)]
    
    # Convert input string to numerical values (0 for 'a', ..., 25 for 'z')
    s = [ord(c) - ord('a') for c in input_str]
    
    # Fill frequency and max frequency for consecutive patterns
    for i in range(N - 2):
        if s[i + 1] == s[i + 2]:
            freq[s[i]][s[i + 1]] += 1
            maxfreq[s[i]][s[i + 1]] += 1
    
    # Check and adjust frequencies for each character replacement
    for i in range(N):
        for c in range(26):
            for j in range(i - 1, i + 2):
                if 0 <= j - 1 and j + 1 < N and s[j] == s[j + 1]:
                    freq[s[j - 1]][s[j]] -= 1

            old_c = s[i]
            s[i] = c
            for j in range(i - 1, i + 2):
                if 0 <= j - 1 and j + 1 < N and s[j] == s[j + 1]:
                    freq[s[j - 1]][s[j]] += 1
                    maxfreq[s[j - 1]][s[j]] = max(maxfreq[s[j - 1]][s[j]], freq[s[j - 1]][s[j]])
            for j in range(i - 1, i + 2):
                if 0 <= j - 1 and j + 1 < N and s[j] == s[j + 1]:
                    freq[s[j - 1]][s[j]] -= 1
            s[i] = old_c

            for j in range(i - 1, i + 2):
                if 0 <= j - 1 and j + 1 < N and s[j] == s[j + 1]:
                    freq[s[j - 1]][s[j]] += 1

    # Generate answers based on max frequencies
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = []
    for a in range(26):
        for b in range(26):
            if a != b and maxfreq[a][b] >= F:
                moo = alphabet[a] + alphabet[b] * 2
                ans.append(moo)
    
    # Output results
    print(len(ans))
    for moo in ans:
        print(moo)


if __name__ == "__main__":
    main()