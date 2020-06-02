from collections import deque
def bfs(v,visited,adj):
    count = 0 
    q = deque([[v,count]])
    while q:
        tmp = q.popleft()
        v = tmp[0]
        count = tmp[1]
        if visited[v] == -1:
            visited[v] = count
            count +=1
            for e in adj[v]:
                q.append([e,count])
                
def solution(n,edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1,visited,adj)
    for v in visited:
        if v == max(visited):
            answer +=1
    return answer
