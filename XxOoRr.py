from math import ceil
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    frequency = []
    for j in range(32):
        frequency.append(0)

    for j in arr:
        string = bin(j)[2:]
        for x in range(len(string)):
            if string[len(string)-x-1] == "1":
                frequency[x] += 1

    operations = 0
    for j in frequency:
        operations += int(ceil(j / k))
    print(operations)