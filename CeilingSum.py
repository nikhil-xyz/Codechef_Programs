from math import ceil

t = int(input())
for i in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
        continue

    if b > a:
        print(int((b-a)/2)+1)
    else:
        if (abs(a-b)%2) != 0:
            print(int((b-a)/2))
        else:
            print(int((b - a) / 2) + 1)