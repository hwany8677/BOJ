#a: bus, b: subway, n: walk to station 
#N이 왜 상관이없지????????
#아 ㅅㅂ 개ㅂㅅ
n,a,b=map(int,input().split())
print("Anything" if a==b else "Bus" if a<b else "Subway")
