def solution(s):
    alpha=list(s)
    stack=[]
    for i in alpha:
        if len(stack)==0:
            stack.append(i)
            continue
        if stack[-1] == i :
            stack.pop()
            continue
        stack.append(i)
    if len(stack)==0:
        return 1
    else:
        return 0
