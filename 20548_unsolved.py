#Filthy code
#문제가 무슨 말을 하려는지 파악을 못하겠
#1*7^0=1
#2*7^0=2
#1*7^1=7
#1*7^0+1*7^1=8
#2*7^0+1*7^1=9
#2*7^1=14
#...and so on
level=[0]
for i in range(1,3):
    for j in range(7): level.append(i*(7**j))
    if i==1:
        for j in range(7):
            level.append(i*(7**j)+i*(7**j))
            level.append(i*(7**j)+i*(7**j)+i*(7**j))
            level.append(i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j))
            level.append(i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j))
            level.append(i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j))
            level.append(i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j)+i*(7**j))
    for j in range(7):
        for k in range(j+1,7): level.append(i*(7**j)+i*(7**k)) 
 
    for j in range(7):
        for k in range(j+1,7):
            for l in range(k+1,7): level.append(i*(7**j)+i*(7**k)+i*(7**l))

    for j in range(7):
        for k in range(j+1,7):
            for l in range(k+1,7):
                for m in range(l+1,7): level.append(i*(7**j)+i*(7**k)+i*(7**l)+i*(7**m))

    for j in range(7):
        for k in range(j+1,7):
            for l in range(k+1,7):
                for m in range(l+1,7):
                    for n in range(m+1,7): level.append(i*(7**j)+i*(7**k)+i*(7**l)+i*(7**m)+i*(7**n))

    for j in range(7):
        for k in range(j+1,7):
            for l in range(k+1,7):
                for m in range(l+1,7):
                    for n in range(m+1,7): 
                        for o in range(n+1,7): level.append(i*(7**j)+i*(7**k)+i*(7**l)+i*(7**m)+i*(7**n)+i*(7**o))
level=list(set(level))
level.sort()
print(level.index(int(input())))