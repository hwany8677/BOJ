#n: Number of jobs
#m: Position of the job
def pQueue(n,m,prio):
	t=0
	while(True):
		max=0
		for i in range(0,len(prio)):
			if prio[i]>=max: max=prio[i]
		if max==prio[0]:
			if m!=0:
#				print("Popped, but wasn't the one")
				prio.pop(0)
				t+=1
				m-=1
#				print(prio)
#				print(f"(Current position: {m})")
			else:
#				print("Popped!")
				t+=1
				return t
		elif max!=prio[0]:
#			print("Not maximum! Moving the queue.")
			prio=[prio[i] for i in range(1,len(prio))] + [prio[0]]
#			print(f"Current queue: {prio}")
			if m==0: 
				m=len(prio)-1
#				print("(Value m reset was performed.)")
			else: m-=1
#			print(f"(Current position: {m})")
tcase=int(input())
for tc in range(0,tcase):
	n,m=map(int,input().split())
	prio=list(map(int,input().split()))
	print(pQueue(n,m,prio))
