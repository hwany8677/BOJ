#놀랍게도 이게 답임
n=int(input())
orb=list(map(int,input().split()))
orb.sort()
length=0
for i in range(len(orb)-1,-1,-1):
    length+=abs(orb[i]-orb[i-1])
print(length)