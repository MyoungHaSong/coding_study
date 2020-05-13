def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    lt = 0
    rt = distance
    while lt <= rt:
        middle = (lt + rt)//2
        init = 0
        mins = distance
        remove = 0
        for i in range(len(rocks)):
            if rocks[i] - init < middle:
                remove +=1
            else:
                mins = min(mins, rocks[i] -init)
                init = rocks[i]
        if remove > n:
            rt = middle -1
        else:
            answer = mins
            lt = middle +1 
            
    return answer