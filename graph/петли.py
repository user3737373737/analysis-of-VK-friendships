lst = [list(map(int, input().split())) for i in range(int(input()))]
flag = 'NO'
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][i] == 1:
            flag = 'YES'
print(flag)