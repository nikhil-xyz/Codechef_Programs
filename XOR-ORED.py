from functools import reduce
t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    temp = []
    for i in range(32):
        temp.append(0)

    for i in arr:
        string = bin(i)[2:]
        k = 31
        for j in range(len(string)-1, -1, -1):
            if string[j] == "1":
                temp[k] += 1
            k -= 1

    flag = False
    string = ""
    for i in range(32):
        if flag:
            if temp[i] > 0:
                string += "1"
            else:
                string += "0"
        else:
            if temp[i] > 0:
                string = "1"
                flag = True
    result1 = int(string, 2)

    for i in range(n):
        arr[i] = arr[i] ^ result1

    result2 = 0
    for i in arr:
        result2 = result2 | i
    print(result1, result2)