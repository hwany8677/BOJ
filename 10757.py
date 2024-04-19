#import os
a,b=map(list,input().split()) 
n=len(a) if len(a)>len(b) else len(b) #Longest number first
sum=[0 for i in range(0,10000)]
a.reverse()
b.reverse()
for i in range(0,n): #Reverse
    temp=int(a[i])+int(b[i])
    if temp>=10: 
        sum[i+1]+=1
        sum[i]+=temp-10
    else: sum[i]+=temp
#    print(f"Current sum: {sum[i]}")
#    os.system("pause")
sum.reverse()
sum=str(sum)
print(int(sum))
#f=open("./meh.txt","w")
#for i in sum: f.write(f"{i}")
#f.close()