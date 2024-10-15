#가로(W)를 계산하고 세로(H)만 본다
#사람(1)+거리두기(m) (세로, 종축)
#사람(1)+거리두기(n) (가로, 횡축)
h,w,n,m=map(int,input().split()) #크기 및 간격
per_row=1
m_remain=m
## Debug only
#buf=''
#print("*",end=''); buf+='*'
for _ in range(2,w+1):
    if m_remain>0: 
        m_remain-=1
        #print("_",end=''); buf+='_'
    else:
        per_row+=1
        m_remain=m
        #print("*",end=''); buf+='*'
res=per_row
n_remain=n
#print()
for _ in range(2,h+1):
    #print(f"On the row {_}")
    if n_remain>0: 
        n_remain-=1
        #print('-----------------------')
    else:
        res+=per_row
        n_remain=n
        #print(buf)
print(res)
