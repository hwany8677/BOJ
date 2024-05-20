#Pythagorean Theorem
while True:
    buf=list(map(int,input().split()))
    if sum(buf)==0: break
    buf.sort()
    if buf[0]**2 + buf[1]**2 == buf[2]**2: print("right")
    else: print("wrong")