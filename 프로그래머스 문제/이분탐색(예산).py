def solution(budgets, M):
    max_ = 0
    r = max(budgets)
    l = 0
    while l<=r :
        middle = (l +r )//2
        sum_= 0
        for i in budgets:
            if i >middle:
                sum_ += middle
            else:
                sum_ += i
        if sum_ > M:
            r = middle -1
        elif sum_ <=M:
            answer = middle
            l = middle +1
    return answer