lst = [list(map(int, input().split())) for i in range(int(input()))]
flag = 'NO'
for i in range(1, len(lst)):
    for j in range(i):
        if lst[i][i] == 1 and lst[i][j] == lst[j][i]:
            flag = 'YES'
print(flag)