#어디서 많이 봤는데 이 문제...
while True:
    s=list(map(int,input().split()))
    if s[0]==s[1]==s[2]==0: break
    if s[1]-s[0]==s[2]-s[1]: print(f"AP {s[2]+(s[1]-s[0])}")
    elif s[1]/s[0]==s[2]/s[1]: print(f"GP {s[2]*(int(s[1]/s[0]))}")