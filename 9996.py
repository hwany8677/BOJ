input=open(0).readline
n=int(input())
s=input().rstrip().split('*')
for _ in range(n):
    front,back=False,False #매치 여부
    buf=input().rstrip()
    idx=0 #idx==len(s[0])-1, idx==len(s[1])-1 이면 True로 전환
    i=0
    while(i<len(buf)):
        if buf[i]==s[0][idx]: idx+=1
        elif idx!=0: i+=1; break
        if idx==len(s[0]): front=True; i+=1; break
        i+=1
    idx=0
    while(i<len(buf)):
        if buf[i]==s[1][idx]: idx+=1
        elif idx!=0: break
        if idx==len(s[1]): back=True; break
        i+=1
    print("DA" if (front and back) else "NE")