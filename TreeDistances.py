t = int(input())
for i in range(t):
    x, y = map(int, input().split())

    temp = x + y
    temp = int(pow(temp, 0.5))
    if (temp * temp) != (x + y):
        print("NO")
        continue
    else:
        n = temp
        temp_y = 0
        j = 1
        flag = False
        while j <= int(n/2):
            temp_y = 2 * j * (n-j)
            if temp_y == y:
                flag = True
                break
            j += 1

        if flag is not True:
            print("NO")
            continue

        print("YES")
        print(n)
        for k in range(2, (n-j)+2):
            print(1, k, sep=" ", end="\n")

        m = 2
        for k in range(n-j+2, n+1):
            print(m, k, sep=" ", end="\n")
            m += 1

