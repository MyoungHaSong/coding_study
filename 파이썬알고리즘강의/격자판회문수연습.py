import sys
sys.stdin = open('input.txt','rt')
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt +=1
        for z in range(2):
            if a[i+z][j] != a[i+5-z-1][j]:
                break
        else:
            cnt +=1
print(cnt)