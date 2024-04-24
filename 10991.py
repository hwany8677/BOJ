"""Things I need:
1. Main loop (for i in range(0,n))
2. First spacing (for j in range(0,n-i-1))
3. Star and spacing repeating (for k in range(1,2*i), * if k%2 else (space))
"""
n=int(input())
for i in range(1,n+1):
	for j in range(0,n-i): print(" ",end='')
	for k in range(1,2*i):
		if k%2: print("*",end='')
		else: print(" ",end='')
	print()
