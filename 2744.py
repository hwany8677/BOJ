#A: 65 <----- diff: 32 -----> a: 97
s=input()
for i in s:
	if ord(i)<97: print(chr(ord(i)+32),end='')
	else: print(chr(ord(i)-32),end='')
print()
