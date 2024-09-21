#Complete rewrite
L,R,A=map(int,input().split())
#L>R, L<R인 경우를 나누고 L=R 될때까지 반복
while (L!=R and A>0):
    if L<R: L+=1
    elif L>R: R+=1
    A-=1
while (L!=R):
    if L<R: R-=1;
    elif L>R: L+=1;
print(L+R+(A//2)*2)