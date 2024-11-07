#RP RS PS
#Rock beats Scissors, Scissors beat Paper, Paper beats Rock 
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    robots_seq=[]
    for __ in range(n): robots_seq.append(input().rstrip())
    k=len(robots_seq[0])
    survived=[1 for _ in range(n)]
    last_survive=0
    for i in range(k):
        rps=[0,0,0] #R,P,S
        #수가 적으므로 처음부터 끝까지 확인
        for j in range(n):
            if survived[j]==0: continue
            if robots_seq[j][i]=='R': rps[0]=1
            if robots_seq[j][i]=='P': rps[1]=1
            if robots_seq[j][i]=='S': rps[2]=1
        if sum(rps)!=2: continue
        #[1,0,1], [0,1,1], [1,1,0]
        if rps==[1,0,1]:
            for j in range(n):
                if survived[j]==0: continue
                if robots_seq[j][i]=='S': survived[j]=0
        elif rps==[0,1,1]:
            for j in range(n):
                if survived[j]==0: continue
                if robots_seq[j][i]=='P': survived[j]=0
        elif rps==[1,1,0]:
            for j in range(n):
                if survived[j]==0: continue
                if robots_seq[j][i]=='R': survived[j]=0
        if sum(survived)==1:
            for j in range(n):
                if survived[j]: last_survive=j
            last_survive+=1
            print(last_survive)
            break
    if not(last_survive): print(0)