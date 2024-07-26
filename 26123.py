#from time import process_time as p
n,d=map(int,input().split())
buf=list(map(int,input().split()))
#t0=p()
laser=0
mx_idx=buf.index(max(buf))
for _ in range(d):
    if buf[mx_idx]==0: break
    buf[mx_idx]-=1
    laser+=1
#buf[mx_idx]보다 높은애들을 빼서 laser에 더하기
for i in range(len(buf)):
    if buf[i]>=buf[mx_idx]:
        laser+=buf[i]-buf[mx_idx]
#t=p()
#print(t-t0,"seconds")
print(laser)