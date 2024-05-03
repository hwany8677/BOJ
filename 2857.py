s=[]
for i in range(0,5): s.append(input())
c=[]
for i in range(0,5):
	for j in range(0,len(s[i])-2):
		if s[i][j]=='F' and s[i][j+1]=='B' and s[i][j+2]=='I': c.append(i+1)
print(c)
if len(c):
	for i in c: print(f"{i} ",end='')
else: print("HE GOT AWAY!")
