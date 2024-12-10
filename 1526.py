#스레기같이 풀기
n=int(input())
while(n>0):
    str_n=str(n)
    count=0
    to_break=False
    for num in str_n: 
        if num!='4' and num!='7': count+=1
    if count==0: 
        print(n)
        exit(0)
    n-=1