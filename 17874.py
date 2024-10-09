n,h,v=map(int,input().split())
res=[h*v*4,(n-h)*v*4,h*(n-v)*4,(n-h)*(n-v)*4]
print(max(res))