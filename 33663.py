h_lo,h_hi=map(int,input().split())
s_lo,s_hi=map(int,input().split())
v_lo,v_hi=map(int,input().split())
r,g,b=map(int,input().split())
M=max([r,g,b])
m=min([r,g,b])
V=M
S=255*((V-m)/V)
if M==r: H=(60*(g-b))/(V-m)
elif M==g: H=(120+(60*(b-r))/(V-m))
elif M==b: H=(240+(60*(r-g))/(V-m))
if H<0: H+=360
h_in_range=(H)>=h_lo and (H)<=h_hi
s_in_range=(S)>=s_lo and (S)<=s_hi
v_in_range=(V)>=v_lo and (V)<=v_hi
if h_in_range and s_in_range and v_in_range: print("Lumi will like it.")
else: print("Lumi will not like it.")