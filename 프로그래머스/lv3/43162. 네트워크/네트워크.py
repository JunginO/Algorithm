from collections import deque

def solution(n, computers):

    def bfs(index):
        queue=deque()
        queue.append(index)
        
        while queue:
            current_queue = queue.popleft()
            visited[current_queue]=1
            for i in range(n):
                if computers[current_queue][i] and not visited[i]:
                    queue.append(i)
        
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i] :
            bfs(i)
            answer+=1
    
    return answer