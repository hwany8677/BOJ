#일본어를 모르지만 아무튼 해시맵인것 같다
input=open(0).readline
names=dict()
score=[]
n_pos=0
name_len_mx=0
for _ in range(int(input())):
    buf=input().rstrip().split()
    name=buf[0]
    sc=int(buf[1])
    if name not in names: 
        names[name]=n_pos
        score.append(0)
        n_pos+=1
        if len(name)>name_len_mx: name_len_mx=len(name)
    score[names[name]]+=sc
zipped=list(zip(names,score))
zipped.sort()
for i in range(1,1+name_len_mx):
    for element in zipped:
        if len(element[0])!=i: continue
        else: print(element[0],element[1])
