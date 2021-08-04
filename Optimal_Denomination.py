from math import gcd
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(1)
        continue

    temp1 = []
    temp = 0
    temp1.append(0)
    for j in range(1, n):
        temp = gcd(temp, arr[j-1])
        temp1.append(temp)

    temp2 = []
    temp = 0
    temp2.append(0)
    for j in range(n-2, -1, -1):
        temp = gcd(temp, arr[j+1])
        temp2.append(temp)
    temp2.reverse()
    # print(temp1, temp2)

    denomination = 0
    for j in range(n):
        denomination = max(denomination, gcd(temp1[j], temp2[j]))
    # print(denomination)

    temp = 0
    result = 0
    max_value = 0
    for j in range(n):
        if (arr[j] % denomination) == 0:
            result += int(arr[j] / denomination)
            max_value = max(max_value, int(arr[j] / denomination))
        else:
            temp += 1

    if temp > 0:
        print(result + 1)
    else:
        result -= (max_value - 1)
        print(result)

