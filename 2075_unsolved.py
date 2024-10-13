n=int(input())
buf=[1000000007] #최대 힙
#자식노드 좌 = 2n 우 = 2n+1
length=0
for _ in range(n):
    input_buf=list(map(int,input().split()))
    for num in input_buf:
        if length==0:
            buf.append(num)
            length+=1
        else:
            buf.append(num)
            length+=1
            josang=length//2
            element_pos=length
            while (josang>0):
                if buf[josang]<=buf[element_pos]: buf[josang],buf[element_pos]=buf[element_pos],buf[josang]
                josang//=2
                element_pos//=2
    print(buf)
print(buf[n])