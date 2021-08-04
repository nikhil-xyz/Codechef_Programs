t = int(input())

for i in range(t):
    n, e, h, a, b, c = map(int, input().split())

    cakes = min(e, h)
    eggs_available = max(e-cakes, 0)
    bars_available = max(h-cakes, 0)
    if (cakes + int(eggs_available/2) + int(bars_available/3)) < n:
        print(-1)
        continue

    minimum = 1000000000000000
    j = min(cakes, n)
    while j >= 0:
        eggs_available = e - j
        bars_available = h - j
        temp = j * c
        temp1, temp2 = 0, 0
        if a < b:
            temp1 = min(int(eggs_available / 2), n - j)
            temp += temp1 * a
            temp2 = min(int(bars_available / 3), n - j - temp1)
            temp += temp2 * b
        else:
            temp1 = min(int(bars_available / 3), n - j)
            temp += temp1 * b
            temp2 = min(int(eggs_available / 2), n - j - temp1)
            temp += temp2 * a
        if (temp1 < 0) & (temp2 < 0):
            j -= 1
            continue
        if (j + temp1 + temp2) < n:
            j -= 1
            continue
        if temp < minimum:
            minimum = temp
        j -= 1
    print(minimum)
