q = int(input())
for i in range(q):
    n = int(input())
    temp1 = list(map(int, input().split()))
    temp2 = list(map(int, input().split()))
    frogs = list()
    for j in range(n):
        temp = list()
        temp.append(temp1[j])
        temp.append(temp2[j])
        frogs.append(temp)
    frogs.sort()
    indexes = list()
    index = 0
    for j in temp1:
        temp = list()
        temp.append(j)
        temp.append(index)
        index += 1
        indexes.append(temp)
    indexes.sort()
    x = 1
    current_index = indexes[0][1]
    count = 0
    diff = 0
    while x < n:
        if indexes[x][1] <= current_index:
            diff = current_index - indexes[x][1] + 1
            count += int(diff/frogs[x][1])
            current_index = indexes[x][1]+((int(diff/frogs[x][1]))*frogs[x][1])
            if (diff % frogs[x][1]) != 0:
                count += 1
                current_index += frogs[x][1]
        else:
            current_index = indexes[x][1]
        x += 1
    print(count)