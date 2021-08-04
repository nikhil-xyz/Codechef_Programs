n = int(input())
string = list()
for i in range(n):
    string.append(input())

first_string = string[0]
arr = list()
flag = False
for i in string:
    flag = False
    count = -1
    for j in range(0, len(i)):
        string1 = i[j:len(i)]
        string2 = i[0:j]
        count += 1

        if (string1+string2) == first_string:
            flag = True
            arr.append(count)
            break
    if flag == False:
        break
if flag == False:
    print(-1)
    exit(0)

minimum = sum(arr)
for i in range(1, len(string[0])):
    arr = list(map(lambda x: (x+1) % len(string[0]), arr))
    if sum(arr) < minimum:
        minimum = sum(arr)
print(minimum)
