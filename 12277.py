input=open(0).readline

for _ in range(int(input())):
    buf=input().rstrip().split()
    output_buf=[]
    phone=buf[0]
    method=buf[1].split('-')
    i=0
    for cap in method:
        cp=int(cap)
        streak=[0,0,0,0,0,0,0,0,0,0]
        while(cp>0):
            phone[i]
            i+=1