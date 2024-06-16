#문제가 무슨 말을 하려는지 파악을 못하겠
#1*7^0=1
#2*7^0=2
#1*7^1=7
#1*7^0+1*7^1=8
#2*7^0+1*7^1=9
#2*7^1=14
#...and so on
level=[1*(7**i) for i in range(7)]
for i in range(7): level.append(2*(7**i))
for i in range(6):
    for j in range(1,3): level.append(j*(7**i)+j*(7**(i+1)))