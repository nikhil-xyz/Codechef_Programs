import collections
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    frequency = collections.Counter(arr)
    if x == n:
        print(0)
    else:
        temp = 0
        for j in frequency:
            temp += (frequency[j] - 1)
        if temp >= x:
            print(len(frequency))
        else:
            print(len(frequency) - (x - temp))
