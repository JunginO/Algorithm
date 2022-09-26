def solution(s):
    lst=[]
    result=s.split(" ")
    for i in result:
        lst.append(int(i))
    
    answer = str(min(lst))+" "+str(max(lst))
    print(answer)
    return answer