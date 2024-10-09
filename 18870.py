#사전으로 구현
n=int(input())
buf=list(map(int,input().split()))
buf_sorted=sorted(buf)
count=0
seen=buf_sorted[0]
buf_dict={buf_sorted[0]: 0}
for i in range(n):
    if buf_sorted[i]==seen: continue
    else:
        count+=1
        seen=buf_sorted[i]
        buf_dict[seen]=count
res=[]
for element in buf: res.append(buf_dict[element])
print(*res) 
