def solution(n, k, cmd):
    answer = ["O"]*n
    stack=[]
    up=[i-1 for i in range(n+2)]
    down=[i+1 for i in range(n+1)]
    k+=1
    
    for com in cmd:
        a=list(com.split(" "))
        if a[0] == 'C':
            stack.append(k)
            up[down[k]] = up[k]
            down[up[k]]= down[k]
            k= up[k] if n < down[k] else down[k]
        elif a[0] == 'Z':
            backup=stack.pop()
            down[up[backup]]=backup
            up[down[backup]]=backup
        elif a[0] == 'U':
            for _ in range(int(a[1])):
                k=up[k]
        elif a[0] == 'D':
            for _ in range(int(a[1])):
                k=down[k]
    for i in stack:
        answer[i-1]="X"
        
    return "".join(answer)