def solution(N, stages):

    data=[0]*(N+2)
    dic={}
    all_cnt=len(stages)
    for i in stages:
        data[i]+=1
    for i in range(1,N+1):
        if data[i]==0:
            dic[i]=0
        else:
            dic[i]=data[i]/all_cnt
            all_cnt-=data[i]

    dic=sorted(dic, key= lambda x:dic[x], reverse=True)
    
    return dic