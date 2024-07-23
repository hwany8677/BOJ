#5개씩 자르기
#10157과 비슷하게 짜야함 (근데 소스를 못읽음 :skull::skull:)
def seek(): 
    mode=1
    k=R*C
    i=0
    while(i<=k)
for _ in range(int(input())):
    buf=input().split()
    R,C=int(buf[0]),int(buf[1])
    mtrx=[]
    i=0
    buf=buf[2]
    while(i<len(buf)):
        mtrx.append(buf[i:i+C])
        i+=C
    visited_map=[]
    for _ in range(R): visited_map.append([0 for _ in range(C)])
    #방문여부를 알아야 턴을 하지
    print(seek())