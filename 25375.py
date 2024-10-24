#풀이 이해하는데 한 세월
#헛짓거리에 한 세월
#정수론은 어렵다 :blobimfine:
input=open(0).readline
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(1 if a*2<=b and b%a==0 else 0)
