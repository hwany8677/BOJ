a=int(input())
x=int(input())
pre_calc=[] #Starting from a^1
i=1
while(i<x):
    to_append=a**i
    pre_calc.append(to_append)
    i+=i
