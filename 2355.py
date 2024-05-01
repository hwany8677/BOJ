#Easy. Instant.
#from time import process_time
a,b=map(int,input().split())
if a>b: a,b=b,a
#t0=process_time()
print(int((b*(b+1)-a*(a-1))/2))
#t=process_time()
#print(f"Time elapsed on calculation: {t-t0}")
