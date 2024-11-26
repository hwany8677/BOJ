from copy import copy
def permute(s,idx,status):
    copy_s=copy(s)
    res=[]
    if idx==len(s): return [s]
    for i in range(idx,len(s)): #idx <-> i swap
        copy_s=copy(s)
        copy_s[idx],copy_s[i]=copy_s[i],copy_s[idx]
        if status: print(copy_s,i+1)
        res+=permute(copy_s,i+1,0)
    return res
s=list(input())
if s=='100000': print('000001'); exit(0)
s.sort()
res=permute(s,0,1)