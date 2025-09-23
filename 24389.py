n=int(input())
bosu=~n+1+2**32
bin_n=bin(n).split('b')[1].zfill(32)
bin_bosu=bin(bosu).split('b')[1].zfill(32)
count=0
for i in range(32):
    if bin_n[i]!=bin_bosu[i]: count+=1
print(count)