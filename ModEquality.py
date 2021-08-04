t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    smallest = min(arr)
    count = 0
    for i in arr:
        if i == smallest:
            continue
        if (i % 2) == 0:
            if (int(i / 2) - 1) < smallest:
                count = -1
                break
        else:
            if int(i / 2) < smallest:
                count = -1
                break
    if count == -1:
        print(n)
    else:
        print(n - arr.count(smallest))

