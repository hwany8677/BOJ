#10c2 = 45 => 난쟁이 두명을 브루트포스로 배제할꺼임
input=open(0).readline
buf=[]
for _ in range(9): buf.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        res=[]
        sigma=0
        for k in range(9):
            if k==i or k==j: continue
            else: 
                sigma+=buf[k]
                res.append(buf[k])
                if sigma==100 and len(res)==7:
                    for element in res: print(element)
                    exit(0)
