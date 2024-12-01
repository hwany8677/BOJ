#Spaghetti code :<
#n: 리스트에 있는 점수, p: 랭킹 리스트에 올라 갈 수 있는 점수 (실제 리스트의 길이)
n,new,p=map(int,input().split())
if n==0: print(1); exit(0)
scores=list(map(int,input().split()))
scores.append(new)
scores.sort(reverse=True)
pos=1; bonus=0
prev=scores[0]; found=[]
pos_info=[]
# print(prev)
#Position indexing
for i in range(len(scores)):
    score=scores[i]
    if i==0: #ㅅㅂ 이런거 싫은데
        if score==new: found.append(i)
        pos_info.append(pos)
        prev=score
        pos+=1
        continue
    else:
        if prev==score: bonus+=1
        else: bonus=0
        if score==new: found.append(i)
        pos_info.append(pos-bonus)
        prev=score
        pos+=1
#If duplicate is happened to be found outside given range P, print -1
if max(found)>(p-1): print(-1)
else: print(pos_info[max(found)])