w,h,d=map(int,input().split())
if w<=(d*2) or h<=(d*2): print(0)
else: print((w-d-d)*(h-d-d))
