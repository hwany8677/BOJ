#애라이 ## 추가 공백을 출력할바엔 조건 붙이지마 쫌 진짜 왜 사람 40분 시간날리게 만드냐고
for k in range(int(input())):
    p,c,u,r=[],[],[],[]
    n,m=map(int,input().split()) #n: number of patient visits, m: number of machines on candidate list
    usage_list=[0 for _ in range(m)] #for individual machines
    total=[0 for _ in range(m)]
    for i in range(m):  #Machine info input
        buf1,buf2,buf3,buf4=map(int,input().split())
        p.append(buf1)
        c.append(buf2)
        u.append(buf3)
        r.append(buf4)
    for i in range(n): #Simulate
        use=int(input())
        if u[use-1]==0: continue
        usage_list[use-1]+=1
        u[use-1]-=1
    for i in range(m):
        total[i]=usage_list[i]*(r[i]-c[i])-p[i]
    print(f"Data Set {k+1}:")
    for i in range(m):
        if total[i]>0: print(i+1)
    print()