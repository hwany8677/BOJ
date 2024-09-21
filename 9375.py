from sys import stdin
input=stdin.readline

fact_precalc=[1]
temp=1
for i in range(1,31):
    temp*=i
    fact_precalc.append(temp)
for _ in range(int(input())):
    cat_set=set()
    n=int(input())
    res=0
    for _ in range(n):
        name,cat=input().split()
        cat_set.add(cat)
    res+=n 
    length=len(cat_set)
    for r in range(1,length+1):
        temp=int(fact_precalc[length]/(fact_precalc[r]*fact_precalc[length-r]))
        res+=temp
    print(res-1)