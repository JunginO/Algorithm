from collections import deque
def solution(maps):
    answer = 0
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    n=len(maps)
    m=len(maps[0])
    visited=[[0 for _ in range(m)] for _ in range(n)]

    q=deque()
    lst=[]
    q.append([0,0,1])
    while (q):
        x,y,dist=q.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<m:
                if visited[cx][cy]==0 and maps[cx][cy]==1:
                    if cx==(n-1) and cy==(m-1):
                        lst.append(dist+1)
                    else:
                        visited[cx][cy]=1
                        q.append([cx,cy,dist+1])
    if len(lst)==0:
        answer=(-1)
    else:
        lst.sort()
        answer=lst[0]
    
    return answer