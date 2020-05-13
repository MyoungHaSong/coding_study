def solution(n, times):
    max_ = max(times)*n
    min_ = 1
    answer = 0
    while min_ <= max_:
        middle = (max_ + min_) // 2 
        count = 0
        for i in times:
            count += middle // i
        if count >= n :
            answer = middle
            max_ = middle-1
        else:
            min_ = middle+1
        
    return answer