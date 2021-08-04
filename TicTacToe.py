t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())

    moves = []
    for j in range(n * m):
        temp = list(map(int, input().split()))
        moves.append(temp)

    if k == 1:
        print("Alice")
        continue

    start, end, ans = 0, n * m - 1, n * m
    while start <= end:
        mid = int((start + end) / 2)
        matrix = []
        for x in range(n + 1):
            temp = []
            for y in range(m + 1):
                temp.append(0)
            matrix.append(temp)
        for x in range(mid + 1):
            if (x % 2) == 0:
                matrix[moves[x][0]][moves[x][1]] = 1
            else:
                matrix[moves[x][0]][moves[x][1]] = -1
        # prefix sum calculation
        for x in range(1, n+1):
            for y in range(1, m+1):
                matrix[x][y] = matrix[x][y] + matrix[x - 1][y] + matrix[x][y - 1] - matrix[x - 1][y - 1]

        found = False
        for x in range(k, n+1):
            for y in range(k, m+1):
                addition = matrix[x][y] - matrix[x - k][y] - matrix[x][y - k] + matrix[x - k][y - k]
                if abs(addition) == (k * k):
                    found = True
                    break
            if found:
                break

        if found:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    if ans == (m * n):
        print("Draw")
    elif (ans % 2) == 0:
        print("Alice")
    else:
        print("Bob")


