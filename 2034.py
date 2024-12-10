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
    #print(f"START = {oomgae[pos]}")
    start,end=pos,0
    to_continue=False
    for j in range(n): 
        ch=abs(chart[j])%12
        if chart[j]>0: pos+=ch
        else: pos-=ch
        if pos<0: pos+=12
        if pos>11: pos-=12
        if j==n-1: end=pos
        #print(f"ch={ch}, pos={oomgae[pos]}")
        if pos not in startpoint:
            to_continue=True
            break
        # print(pos)
    #if len(oomgae[pos])==2 or len(oomgae[start])==2 or len(oomgae[end])==2: continue
    if to_continue: continue
    else: print(oomgae[start],oomgae[end])
    # print("---- cut ----")
