input=open(0).readline
n=int(input())
i=1
while(n!=0):
    towns=[]
    for _ in range(n): towns.append(input().rstrip())
    towns=list(set(towns))
    print(f"Week {i} {len(towns)}")
    n=int(input())
    i+=1
