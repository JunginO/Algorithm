n=int(input())
lst=list(map(int,input().split()))
plus,minus,mul,div=map(int,input().split())

max_val=-1e9
min_val=1e9

def dfs(i,now):
    global min_val,max_val,plus,minus,mul,div

    if i==n:
        min_val=min(min_val,now)
        max_val=max(max_val,now)
    else:
        if plus>0:
            plus-=1
            dfs(i+1,now+lst[i])
            plus+=1
        if minus>0:
            minus-=1
            dfs(i+1,now-lst[i])
            minus+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*lst[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/lst[i]))
            div+=1
dfs(1,lst[0])
print(max_val)
print(min_val)