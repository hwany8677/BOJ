#파이썬은 너무 날먹
#from time import process_time
a,b=map(int,input().split())
if a>b: a,b=b,a #혹시나몰라서
print(b-a-1)
#t0=process_time()
for i in range(a+1,b): print(f"{i} ",end='')
#t=process_time()
#print(f"\nΔt={t-t0}")