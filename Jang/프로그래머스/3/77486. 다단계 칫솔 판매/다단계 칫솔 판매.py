def solution(enroll, referral, seller, amount):
    answer = []
    dic={}
    ref={}
    dic['center']=0
    for i,j in zip(enroll,referral):
        dic[i]=0
        ref[i]=j
    
    for i,j in zip(seller, amount):
        sum_amount=100*j
        curr=i
        while True:
            minus_amount = sum_amount//10
            if minus_amount == 0:
                dic[curr]+=sum_amount
                break
            if ref[curr] =='-':
                dic[curr]+=sum_amount-minus_amount
                dic['center']+=minus_amount
                break
                
            else:
                sum_amount-=minus_amount
                dic[curr]+=sum_amount
                sum_amount=minus_amount
                curr=ref[curr]
    for i in enroll:
        answer.append(dic[i])
    return answer