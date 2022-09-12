n=int(input())
nums=[[],[],[],[],[],[],[],[],[],[]]
solved=[]
keys=[]
num=9
ans=0
for _ in range(n):
    tmp=input()
    current=0
    for i in reversed(range(len(tmp))):
        nums[current].append(tmp[i])
        current+=1
for i in reversed(range(len(nums))):
    if nums[i]:
        for j in nums[i]:
            if j not in solved:
                solved.append(j)
                keys.append(10**i)
            else:
                keys[solved.index(j)]+=(10**i)
keys.sort(reverse=True)
for i in keys:
    ans+=(num*i)
    num-=1
print(ans)