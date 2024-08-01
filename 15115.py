#Local minimum
from math import sqrt,ceil
k,p,x=map(int,input().split()) #Days required, Penalty constant, Payment by each painter
m=ceil(sqrt((k*p)/x))
res=( (k*p)/m )+x*m
print("{:.3f}".format(res))