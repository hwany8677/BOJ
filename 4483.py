input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    names=[]
    for __ in range(n): names.append([input().rstrip(),0])
    d=int(input())
    for __ in range(d):
        data=input().rstrip().split()
        for i in range(n):
            name=names[i][0]
            if name in data: names[i][1]=1
    print(f"Test set {_+1}:")
    for element in names: print(element[0],"is absent" if element[1]==0 else "is present")
    print()