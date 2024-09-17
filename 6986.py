from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
buf=[]
for _ in range(n): buf.append(float(input()))
buf.sort()
length=len(buf)
start=k
end=len(buf)-k
sigma=0
for i in range(start,end): sigma+=buf[i]
t_mean=sigma/(length-(k*2))
t_mean+=0.00000001 #오차보정
print("{:.2f}".format(t_mean))
sigma=0
for i in range(length):
    if i<start: sigma+=buf[start]
    elif i>(end-1): sigma+=buf[end-1]
    else: sigma+=buf[i]
adj_mean=sigma/length
adj_mean+=0.00000001 #오차보정
print("{:.2f}".format(adj_mean))