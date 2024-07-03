from sys import stdin
for _ in range(int(input())):
    n=int(stdin.readline())
    if n==2: print(1,1)
    elif n==3: print(1,2)
    elif n==4: print(2,2)
    elif n==5: print(2,3)
    elif n==7: print(3,4)
    elif n==9: print(4,5)
    elif n==6: print(3,3)
    elif n==8: print(4,4)
    else:
        L=len(str(n))-1
        a,b="",""
        for i in range(2):
            for j in range(1,10):
                a=f"{j}"*L
                b=str(n-int(a))
                noNumber=False
                for k in range(1,len(b)):
                    if b[k-1]!=b[k]:
                        noNumber=True
                        break
                if noNumber: continue
                print(a,b)
                break
            if not(noNumber): break
            L+=1