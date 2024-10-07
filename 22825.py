#Python 3에서 TLE
z=int(input())
while(z>0):
    z3=z**3
    x,y=1,1
    mx=0
    to_break=False
    while(x**3<=z3):
        y=1
        while(y**3<=z3):
            temp=x**3+y**3
            if temp>z3: break
            elif temp>mx: mx=temp
            y+=1
        x+=1
    print(z3-mx)
    z=int(input())
