d1,d2,d3=map(int,input().split())
if not(d2+d3>d1) or not(d3+d1>d2) or not(d1+d2>d3): print(-1)
else:
  print(1)
  a=(0.5)*(d1-d3+d2)
  c=(0.5)*(d2-d1+d3)
  b=(0.5)*(d3-d2+d1)
  print("{:.1f}".format(a),"{:.1f}".format(b),"{:.1f}".format(c))