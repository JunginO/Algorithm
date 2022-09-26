n=int(input())
lst=list(map(int,input().split()))
lst.sort()

ans=1

for i in lst:
    if ans<i:
        break
    ans+=i

print(ans)