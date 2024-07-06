#y축 Sn을 구한거에 또 다른 x축 Sn을 구해야함
#안그러면 1~1024 다 구할때 25초나 걸림
from time import process_time as p
from sys import stdin
def Sn(buf,length):
    S=[buf[0]]
    for k in range(1,length):
        S.append(buf[k]+S[k-1])
    return S
n,m=map(int,input().split()) #Fixed to n by n
buf=[]
SIGMA_Y=[]
# t0=p()
for i in range(n): #최대 소요시간 0.578125초
    buf.append(list(map(int,stdin.readline().split())))
    SIGMA_Y.append(Sn(buf[i],n))
#[[1, 3, 6, 10], [2, 5, 9, 14], [3, 7, 12, 18], [4, 9, 15, 22]]
#필요에 따라 취사선택 후 SIGMA_X에 append
# t=p()
# print(f"List gen took {t-t0} seconds")
sigma=0
for _ in range(m): #10만번 -> 몇십초씩걸림
    x1,y1,x2,y2=map(int,stdin.readline().split())
    # t0=p()
    buf2=[]
    SIGMA_X=[]
    
    # t=p()
    # sigma+=t-t0
# print(f"I/O took {sigma} seconds")