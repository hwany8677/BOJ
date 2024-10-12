n,m=map(int,input().split())
count=0
for _ in range(n):
    letter=[0 for _ in range(27)]
    for i in range(0,m): letter[i]+=1
    s=input()
    to_cont=False   
    for char in s:
        idx=ord(char)-65
        if letter[idx]==0:
            to_cont=True
            break
        letter[idx]-=1
    if to_cont: continue
    count+=1
print(count)
