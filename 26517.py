#이게왜 실5
k=int(input())
a,b,c,d=map(int,input().split())
left_lim=a*k+b
right_lim=c*k+d
f_k=a*k+b
if left_lim == right_lim:
    if f_k == left_lim: print("Yes", f_k)
else: print("No")