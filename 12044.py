for _ in range(int(input())):
    n,k=map(int,input().split())
    candidate=[]
    for _ in range(4): candidate.append(list(map(int,input().split())))
    c=0
    for i in range(n):
        a=candidate[0][i]
        b=candidate[1][i]
        c=candidate[2][i]
        d=candidate[3][i]
        if a^b^c^d==k: c+=1
    
    for i in range(n):
        a=candidate[0][i]
        b=candidate[1][0]
        c=candidate[2][0]
        d=candidate[3][0]
        if a^b^c^d==k: c+=1
    for i in range(n):
        a=candidate[0][0]
        b=candidate[1][i]
        c=candidate[2][0]
        d=candidate[3][0]
        if a^b^c^d==k: c+=1
    for i in range(n):
        a=candidate[0][0]
        b=candidate[1][0]
        c=candidate[2][i]
        d=candidate[3][0]
        if a^b^c^d==k: c+=1
    for i in range(n):
        a=candidate[0][0]
        b=candidate[1][0]
        c=candidate[2][0]
        d=candidate[3][i]
        if a^b^c^d==k: c+=1

    for i in range(n):
        a=candidate[0][i]
        b=candidate[1][i]
        c=candidate[2][0]
        d=candidate[3][0]
        if a^b^c^d==k: c+=1
    