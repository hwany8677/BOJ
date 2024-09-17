from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
buf=[]
print_buf=[]
pbuf_order=-1
for _ in range(3*n): buf.append(input())
for i in range(3*n):
    if not(buf[i][1].isnumeric()): continue
    else:
        print_buf.append([])
        pbuf_order+=1
        for j in range(0,8*m,8):
            a,b=int(buf[i][j+1]),int(buf[i][j+3])
            if buf[i][j+6]!='.': c=int(buf[i][j+5])*10+int(buf[i][j+6])
            else: c=int(buf[i][j+5])
            if a+b==c:
                if buf[i][j+6]=='.':
                    print_buf[pbuf_order].append(".*****..")
                    print_buf[pbuf_order].append(f"*{a}+{b}={c}*.")
                    print_buf[pbuf_order].append(".*****..")
                else:
                    print_buf[pbuf_order].append(".******.")
                    print_buf[pbuf_order].append(f"*{a}+{b}={c}*")
                    print_buf[pbuf_order].append(".******.")
            else:
                if buf[i][j+6]=='.':
                    print_buf[pbuf_order].append(".../....")
                    print_buf[pbuf_order].append(f".{a}/{b}={c}..")
                    print_buf[pbuf_order].append("./......")
                else:
                    print_buf[pbuf_order].append(".../....")
                    print_buf[pbuf_order].append(f".{a}/{b}={c}.")
                    print_buf[pbuf_order].append("./......")
for i in range(pbuf_order+1):
    for j in range(3):
        pbuf_final=[print_buf[i][j+k] for k in range(0,3*(m-1)+1,3)]
        print(*pbuf_final,sep='')