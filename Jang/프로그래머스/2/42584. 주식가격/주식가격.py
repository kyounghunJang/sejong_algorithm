def solution(prices):
    size=len(prices)
    stack=[0]
    answer=[0]*size
    for i in range(1,size):
        
        while len(stack)!=0 and prices[i]<prices[stack[-1]]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)
    while stack:
        j=stack.pop()
        answer[j]=size-1-j        

    return answer