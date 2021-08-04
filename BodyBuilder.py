t = int(input())
for i in range(t):
    n, r = map(int, input().split())

    workout = list(map(int, input().split()))
    gain = list(map(int, input().split()))

    temp = gain[0]
    result = gain[0]
    for j in range(1, n):
        temp1 = (workout[j] - workout[j-1]) * r
        temp = max(0, temp - temp1)
        temp += gain[j]
        result = max(result, temp)
    print(result)
