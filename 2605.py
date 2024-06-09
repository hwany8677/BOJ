n=int(input())
order=list(map(int,input().split()))
line=[]
for i in range(n):
    # if order[i]==0 or order[i]==i: line.append(i+1)
    # else:
    # ^^^^^^^ 저 코드 뺐더니 정답이됨...뭐지??
    left=order[i]
    right=len(line)
    if order[i]==i-1:
        temp=line[len(line)-1]
        line=[line[j] for j in range(left)]+[i+1]
        line.append(temp)
    else: line=[line[j] for j in range(left)]+[i+1]+[line[k] for k in range(left,right)]
line.reverse()
print(*(line))