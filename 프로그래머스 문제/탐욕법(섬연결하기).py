import math
def solution(n, costs):
    answer = 0
    costs = [(w,f,t) for f,t,w in costs]
    costs.sort()
    v = set()
    w,f,t = costs[0]
    if f != t:
        answer +=w
        
    v.update([f,t])
    while len(v) != n:
        _min = math.inf
        for w,f,t in costs:
            if t in v or f in v:
                if (f in v and t in v) or f ==t :
                    continue
                if _min > w:
                    _min = w 
                    frm, to = f,t
        answer += _min
        v.add(frm)
        v.add(to)
    return answer