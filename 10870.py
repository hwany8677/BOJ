#From scratch
#from time import process_time
a,b=0,1
n=int(input())
#t1=process_time()
for i in range(0,n): a,b=b,a+b
#t2=process_time()
print(a)
print(f"Elapsed time: {t2-t1} seconds")

