#시간복잡도 O(n)
#from time import process_time
n=int(input())
s=0
#t0=process_time()
for i in range(0,n): s+=n*i+i
#t=process_time()
print(s)
#print(f"Time took to process: {t-t0} seconds")
