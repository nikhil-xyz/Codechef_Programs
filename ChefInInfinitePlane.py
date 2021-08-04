t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    result = 0
    i = 0
    while i < n:
        j = i+1
        if j < n:
            while arr[j] == arr[j-1]:
                j += 1
                if j == n:
                    break
        available = j - i
        possible = arr[i] - 1
        result += min(available, possible)
        i = j
    print(result)