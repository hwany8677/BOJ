#아 오늘 진짜 되는게 없네
x=int(input())
y=int(input())
if x<2: 
    print("Before")
    exit(0)
elif x>2: 
    print("After")
    exit(0)
else:
    if y<18: print("Before")
    elif y>18: print("After")
    else: print("Special")