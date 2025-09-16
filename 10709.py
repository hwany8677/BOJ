#안 뜨면 -1
input=open(0).readline
h,w=map(int,input().split())
clouds=["" for _ in range(h)]
for i in range(h): clouds[i]=input().rstrip()
for i in range(h):
    encountered=False
    c=0
    for j in range(w):
        cloud=clouds[i][j]
        if cloud=="c":
            encountered=True
            c=0
        elif encountered==False:
            print("-1 ",end='')
            continue
        else: c+=1
        print(c,end=' ')
    print()
