#x^y^y=x
#I hate XOR for passion ffs
from sys import stdin
input=stdin.readline

sigma=0
sigma_xor=0
for _ in range(int(input())):
    read=input().split()
    cmd=read[0]
    try: element=int(read[1])
    except IndexError: element=0
    if cmd=='1': 
        sigma+=element
        sigma_xor^=element
    if cmd=='2': 
        sigma-=element
        sigma_xor^=element
    if cmd=='3': print(sigma)
    if cmd=='4': print(sigma_xor)