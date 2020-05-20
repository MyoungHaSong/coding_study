from collections import deque
def solution(priorities, location):
    priorities = [(p,index) for p, index in enumerate(priorities)]
    priorities = deque(priorities)
    answer = 0
    cnt = 0
    print(priorities)
    
    while priorities:
        tmp = priorities.popleft()
        if all(tmp[1] >= x[1] for x in priorities ):
            cnt +=1
            if location == tmp[0] :
                answer = cnt
                break
        else:
            priorities.append(tmp)
    return answer