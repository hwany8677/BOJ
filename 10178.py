t=int(input())
for i in range(0,t):
    can,sib=map(int,input().split())
    print(f"You get {can//sib} piece(s) and your dad gets {can%sib} piece(s).")