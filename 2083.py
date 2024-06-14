#Great way to start the day
a,b,c=input().split()
name,age,weight=[],[],[]
while (a!='#' and b!='0' and c !='0'):
    name.append(a)
    age.append(int(b))
    weight.append(int(c))
    a,b,c=input().split()
for i in range(len(name)):
    if age[i]>17 or weight[i]>=80: print(f"{name[i]} Senior")
    else: print(f"{name[i]} Junior")