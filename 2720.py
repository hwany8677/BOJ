#25,10,5,1
#어제 그리디를 해서 그런지 갑자기 ptsd가...
input=open(0).readline
for _ in range(int(input())):
    c=int(input())
    count=[0,0,0,0]
    while(c>0):
        if c-25>=0: c-=25; count[0]+=1
        elif c-10>=0: c-=10; count[1]+=1
        elif c-5>=0: c-=5; count[2]+=1
        elif c-1>=0: c-=1; count[3]+=1
    print(*count)
