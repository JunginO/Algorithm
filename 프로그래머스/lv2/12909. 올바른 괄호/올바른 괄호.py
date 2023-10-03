def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        else:
            if not stack:#비어있을경우
                answer = False
                break
            else:
                stack.pop(-1)
    if stack:
        answer = False
                
    return answer