from math import gcd
t = int(input())
for tt in range(t):
    x, y = map(int, input().split())

    if gcd(x, y) > 1:
        print(0)
    elif (gcd(x+1, y) > 1) | (gcd(x, y+1) > 1):
        print(1)
    else:
        print(2)



