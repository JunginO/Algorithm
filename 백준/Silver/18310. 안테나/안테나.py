n=int(input())
lst=list(map(int,input().split()))
lst.sort()
#중간값 구하기
print(lst[(n-1)//2])