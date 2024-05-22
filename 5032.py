#1. 바꾼다
#2. 마신다
#3. 쌓인다
e,f,c=map(int,input().split())
e=e+f
count=0
while True:
    if e<c: break
    e-=c
    e+=1
    count+=1
print(count)