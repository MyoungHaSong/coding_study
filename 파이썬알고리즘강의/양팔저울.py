import sys
sys.stdin = open('input.txt','rt')
def DFS(L,sum):
    # L은 추의 index, sum은 무게
    global res
    if L ==n:
        if 0<sum<= s:
            res.add(sum)

    else:
        DFS(L+1,sum+G[L]) # 왼쪽에 놓는다.
        DFS(L+1, sum-G[L]) # 오른쪽에 놓는다.
        DFS(L+1, sum) # 추를 사용하지 않겠다. 

if __name__ == '__main__':
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set() # 중복을 제거하며 값을 추가할 수 있음.
    DFS(0,0)
    print(s-len(res))