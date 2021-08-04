t = int(input())
for x in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = list()
    for i in range(32):
        freq.append(0)

    for i in range(n):
        temp = bin(arr[i])[2:]
        index = 32 - len(temp)
        for j in range(len(temp)):
            freq[index + j] += int(temp[j])

    result = str()
    for i in range(32):
        if freq[i] > 0:
            result += "1"
    print(int(result, 2))

    for i in range(q):
        x, y = map(int, input().split())

        temp = bin(arr[x - 1])[2:]
        index = 32 - len(temp)
        for j in range(len(temp)):
            freq[index + j] -= int(temp[j])

        arr[x - 1] = y
        temp = bin(arr[x - 1])[2:]
        index = 32 - len(temp)
        for j in range(len(temp)):
            freq[index + j] += int(temp[j])

        result = ""
        flag = False
        for j in range(32):
            if (freq[j] > 0) | flag:
                if freq[j] > 0:
                    result += "1"
                else:
                    result += "0"
                flag = True
        print(int(result, 2))

