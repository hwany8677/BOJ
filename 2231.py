#Check if (number)+(digit+digit+...)=n for every loop
n=int(input())
moving_n=int(n)
gen=[]
while moving_n>0:
  digit=list(str(moving_n))
  for i in range(0,len(digit)): digit[i]=int(digit[i])
  if n==moving_n+sum(digit): gen.append(moving_n)
  moving_n-=1
print(min(gen) if len(gen)!=0 else 0)