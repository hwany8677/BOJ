#C->D->...->G->A->B순으로 가정
#E->F를 가야하는데 +2가 오거나, D->E를 가야하는데 +1가 오거나, C->B를 가야하는데 -2가 올경우 continue
input=open(0).readline
oomgae=[]
for i in range(65,72): 
    oomgae.append(chr(i))
    if i!=66 and i!=69: oomgae.append(chr(i)+'#')
chart=[]
startpoint=[0,2,3,5,7,8,10]
n=int(input())
for _ in range(n): chart.append(int(input()))
for i in startpoint:
    pos=i
    print(f"START = {oomgae[pos]}")
    start,end=0,0
    for j in range(n): 
        ch=abs(chart[j])%12
        # print(f"ch={ch}")
        pos+=ch
        if pos<0: pos+=12
        if pos>11: pos-=12

        if j==0: start=pos
        elif j==n-1: end=pos
        # print(pos)
    if len(oomgae[pos])==2 or len(oomgae[start])==2 or len(oomgae[end])==2: continue
    else: print(oomgae[start],oomgae[end])
    # print("---- cut ----")