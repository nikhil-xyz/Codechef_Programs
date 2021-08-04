t = int(input())
for i in range(t):
    n = int(input())
    string = input()

    count = n
    total_1 = string.count("1")
    if total_1 == 1:
        count = 0
    else:
        factors = []
        for j in range(1, n+1):
            if (n % j) == 0:
                factors.append(j)

        for j in factors:
            count1 = {}
            [count1.setdefault(z, 0) for z in range(j)]
            count0 = {}
            [count0.setdefault(z, 0) for z in range(j)]
            for x in range(n):
                if string[x] == "0":
                    count0[x % j] += 1
                else:
                    count1[x % j] += 1

            for x in range(j):
                count = min(count, count0[x] + (total_1 - count1[x]))

    print(count)





