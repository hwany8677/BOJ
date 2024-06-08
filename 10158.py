from time import process_time as p
s=0
t0=p()
for _ in range(0,200000000,1000): s+=1
t=p()
print(f"2억까지 더하는데 걸린 시간: {t-t0} seconds")