#Falling through whitespace
while(1):
    n=int(input())
    if n==0: break
    pos=1
    for _ in range(n):
        s=input()
        if len(s)-1<pos: continue
        else:
            for i in range(pos-1, len(s)):
                if s[i]==' ': #Spacing
                    pos=i+1
                    break
                if i==len(s)-1: pos=len(s)+1 #End
    print(pos)