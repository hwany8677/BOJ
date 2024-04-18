# 8 x 2 = 16
# 8 and 2 both are factors of 16
# 16 is a multiple of 8 and 2 separately
# first // second = proper integer -> first is a multiple of the second
# second // first = proper integer -> first is a factor of the second
a,b=-1,-1
while(1):
    a,b=map(int, input().split())
    if (a==0 and b==0): break
    if a%b==0 or b%a==0:
        if a//b!=0: print("multiple")
        elif b//a!=0: print("factor")
    else: print("neither")