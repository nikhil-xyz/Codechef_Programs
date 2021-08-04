t = int(input())
for i in range(t):
    D, d, P, Q = map(int, input().split())

    count = D * P
    n = int(D / d)
    count += Q * (n * (n - 1) / 2) * d
    count += (D % d) * Q * n
    print(int(count))
