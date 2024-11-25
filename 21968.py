#흐어어 난 병신이다 이걸 삼진수가 안보이다니
#삼진수 -> 0,1,2
#삼진수 표현: 0,1,2,10,11,12,20,21,22,100,101,102,110,111,112,120,121,122,200,...
#이진수처럼 하면 됨
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    res=''
    while(n>0):
        r=n%3
        q=n//3
        n=q
        if q==0: continue
        res+=str(r)
