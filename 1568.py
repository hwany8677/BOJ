#이게 뭐라고 30분이나 넘게 붙들고 앉아있지????
n=int(input())
go=1
s=0
while(True):
#	print(f"go: {go}, n_before: {n}, ",end='')
	if go>n: go=1
	n-=go
	go+=1
	s+=1
#	print(f"n_after: {n}, ",end='')
	if n==0: break
#	print(f"s: {s}")
print(s)
