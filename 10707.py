#X: A円/L (no limit)
#Y: B円 till CL, +D円 on every +1L
#Uses: PL/month
a=int(input()) #X
b=int(input()) #Y
c=int(input()) #Y's limit
d=int(input()) #Y's extra
p=int(input())
sigX=p*a
sigY=b if p<=c else b+d*(p-c)
print(sigX if sigX<sigY else sigY)