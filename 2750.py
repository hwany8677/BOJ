#1000개 정도론 .sort() 해도됨...
#from time import process_time as p
buf=[]
for _ in range(int(input())): buf.append(int(input()))
#t0=p()
buf.sort()
print(*buf,sep='\n')
# t=p()
# print(f"Time took to process: {t-t0} seconds")