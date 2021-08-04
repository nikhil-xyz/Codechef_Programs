t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    start = arr[int(n/2)-1] - int(k/2)

    result = 100000000000000
    for j in range(start, start+2):
        temp = 0
        hill = j + k - 1
        for x in range(n):
            temp += max(abs(hill - arr[x]), abs(j - arr[x]))
        result = min(temp, result)

    print(result)