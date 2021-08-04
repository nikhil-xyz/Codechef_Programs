t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    odd = []
    even = []
    for j in arr:
        if (j % 2) == 0:
            even.append(j)
        else:
            odd.append(j)

    result = []
    even_count = len(even)
    odd_count = len(odd)

    count = min(even_count, odd_count)
    if (odd_count == 2) & (even_count == 1):
        result.append(odd[0])
        result.append(even[0])
        result.append(odd[1])
    else:
        k = 0
        while k < even_count:
            result.append(even[k])
            k += 1

        k = 0
        while k < odd_count:
            result.append(odd[k])
            k += 1

    print(*result)
