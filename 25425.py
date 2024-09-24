#25%, 25%, 25% WA
#풀었어도 뭘 뭍는 문제인지 감을 못잡겠음
#경우의 수가 도대체 어떻게 되는거임?
n,m,a,k=map(int,input().split())
#1씩 고르게 분포
if (a-k)/n>=1: print(f"{n} ",end='')
else: print(f"{(a-k)+1} ",end='')
temp=(a-k)//m #(30-3)//5=5
t_count=temp #t_count=5
a-=temp*m #5*5=25, 30-25=5
a-=k #5-3=2, 2가 남음
if a>0: t_count+=1 
t_count+=1
print(t_count)
