n1=int(input())
n2=int(input())
n3=int(input())
bin1=(list(bin(n1).split('b')[1])); bin1.reverse()
bin2=(list(bin(n2).split('b')[1])); bin2.reverse()
bin3=(list(bin(n3).split('b')[1])); bin3.reverse()
lsb=['','','']
for i in range(4):
    if len(bin1)>i: lsb[0]+=bin1[i]
    if len(bin2)>i: lsb[1]+=bin2[i]
    if len(bin3)>i: lsb[2]+=bin3[i]
passwd=''
for i in range(3): 
    if len(lsb[i])<4: 
        lsb[i]=lsb[i].zfill(4)
        lsb[i]=list(lsb[i])
    else:
        lsb[i]=list(lsb[i])
        lsb[i].reverse()
    for char in lsb[i]: passwd+=char
final=0
exp=0
for i in range(len(passwd)-1,-1,-1):
    final+=int(passwd[i])*(2**exp)
    exp+=1
final=str(final).zfill(4)
print(final)
