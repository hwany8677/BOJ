from math import ceil
s=input()
n_count=[0 for _ in range(10)]
for num in s:
    if num=='9': n_count[6]+=1
    else: n_count[int(num)]+=1
n_count[6]+=n_count[9]
n_count[9]=0
n_count[6]=ceil(n_count[6]/2)
print(max(n_count))