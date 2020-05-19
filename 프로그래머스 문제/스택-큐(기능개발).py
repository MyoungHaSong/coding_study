from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    stack = []
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                stack.append(progresses.popleft())
                speeds.popleft()
        if len(stack)>0:
            answer.append(len(stack))
            stack = []

    return answer

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]