def solution(want, number, discount):
    answer = 0
    length=len(discount)
    want_dic={}
    for i,j in zip(want,number):
        want_dic[i]=j
    i=10
    while True:
        chk=1
        tmp=discount[i-10:i]
        dic={}
        for j in tmp:
            if j not in dic:
                dic[j]=1
            else:
                dic[j]+=1 
                
        
        if dic == want_dic:
            answer+=1
        
        if i == length+1:
            break
        i+=1
        
    return answer