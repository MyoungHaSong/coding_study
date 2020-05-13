def solution(numbers, target):
    global cnt
    def DFS(L,sum_):
        global cnt
        if L == len(numbers):
            if sum_ ==target:
                cnt +=1
        else:
            DFS(L+1,sum_ + numbers[L])
            DFS(L+1,sum_ - numbers[L])
    cnt = 0
    DFS(0,0)
    return cnt
