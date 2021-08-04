t = int(input())
for tt in range(t):
    n, k = map(int, input().split())

    temp = (pow(2, n) - 1) * 2
    k = min(k, int(pow(2, n) / 2))
    print(k * temp)
