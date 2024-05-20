#42로 나눈 나머지 중 '독특한' 애들 몇 개 있는지 알아보기
#리스트 -> 집합
n=[]
for _ in range(0,10): n.append(int(input()) % 42)
n=set(n)
print(len(n))