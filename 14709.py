#1 3
#3 1
#3 4
#4 3
#1 4
#4 1
pairs=[]
for i in range(int(input())):
    s=tuple(map(int,input().split()))
    if s==(3,1): s=(1,3)
    if s==(4,3): s=(3,4)
    if s==(4,1): s=(1,4)
    pairs.append(s)
if (1,3) in pairs:
    if (3,4) in pairs:
        if (1,4) in pairs:
            if len(pairs)==3:
                print("Wa-pa-pa-pa-pa-pa-pow!")
                exit(0)
print("Woof-meow-tweet-squeek")