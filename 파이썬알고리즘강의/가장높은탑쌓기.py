import sys
sys.stdin = open('input.txt','rt')

if __name__=='__main__':
    n = int(input())
    brisks = []
    for i in range(n):
        a,b,c = map(int, input().split())
        brisks.append((a,b,c))
    brisks.sort(reverse = True)
    dy = [0] * n 
    dy[0] = brisks[0][1]
    res = brisks[0][1]
    for i in range(1,n):
        max_h= 0
        for j in range(i-1,-1, -1):
            if brisks[j][2] > brisks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + brisks[i][1]
        res = max(dy[i], res)
    print(res)