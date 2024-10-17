#111 111 -> 1
#111 1111 -> 1
#111 11111 -> 11?
#111 111111 -> 111
#111 111111111 -> 111
#작은것부터 자릿수 보기
#B의 자릿수가 A의 자릿수의 배수 -> A가 gcd
#A와 B의 자릿수가 전부 짝수 -> 11이 gcd
#그 외 -> 1이 gcd
a,b=map(int,input().split())
if a<b: a,b=b,a
if b%a==0: print("1"*a)
elif a%2==0 and b%2==0: print(11)
else: print(1)
