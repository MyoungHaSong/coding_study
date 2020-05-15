def solution(tickets):
    answer = []
    table = {}
    for s,t in tickets:
        if s in table:
            table[s].append(t)
            table[s].sort(reverse = True)
        else:
            table[s] = [t]
    Q = []
    Q.append('ICN')
    while Q:
        tmp = Q[-1]
        if tmp not in table or len(table[tmp]) == 0 :
            answer.append(Q.pop())
        else:
            Q.append(table[tmp][-1])
            table[tmp].pop()
    answer.reverse()
    return answer