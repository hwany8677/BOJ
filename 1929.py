#특정 구간 사이 찾기 = n을 소인수분해 하는거와 같음
#False: 합성수임
#True: 소수임
#from time import process_time
from math import sqrt
m,n=map(int,input().split())
arr=[]
for _ in range(0,n+1): arr.append(True)
arr[0],arr[1]=False,False
#t0=process_time()
for i in range(2,int(sqrt(n))+1):
#  print(f"Divide {i}!")
  for j in range(i,n+1,i):
#    print(f"Currently inspecting: {j}")
    if not(arr[i]): continue 
    if j%i==0 and j!=i:
#      print("It was not prime.")
      arr[j]=False
#t=process_time()
for i in range(m,n+1):
  if arr[i]: print(i)
#print(f"Took {t-t0} seconds to process")
