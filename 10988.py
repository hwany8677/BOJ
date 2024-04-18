def pal(s):
	start,end=0,len(s)-1
	while(start<=end):
		if s[start]==s[end]: 
			start+=1
			end-=1
			continue
		else: return 0
	return 1
s=input()
print(pal(s))