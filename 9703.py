#오름차순으로 한 번, 내림차순으로 한 번
#쭉 탐색
from sys import stdin
input=stdin.readline

for T in range(int(input())):
    n=int(input())
    buf=list(map(int,input().split()))
    #Check gap -> check non-decreasing or non-increasing
    delta_max=max(buf)-min(buf)
    for delta in range(1,delta_max):
        non_decreasing=False
        for idx_start in range(n):
            count,expected=0,buf[idx_start]
            for i in range(n): #Check
                if expected==buf[i]:
                    count+=1
                    expected+=delta
                if count==3: non_decreasing=True; break
            if non_decreasing: break
        non_increasing=False
        for idx_start in range(n):
            count,expected=0,buf[idx_start]
            for i in range(n): #Check
                if expected==buf[i]:
                    count+=1
                    expected-=delta
                if count==3: non_increasing=True; break
            if non_increasing: break
        #Break immediately whenever it's found
        if non_decreasing or non_increasing: break
    print(f"Case #{T+1}: ",end='')
    if non_decreasing or non_increasing: print("NO")
    else: print("YES")
