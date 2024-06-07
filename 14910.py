#느릴 줄 알았던 코드
from sys import stdin
def P(path):
    for i in range(0,len(path)-1):
        if path[i]>path[i+1]: return "Bad"
    return "Good"
path=list(map(int,stdin.readline().split()))
print(P(path))