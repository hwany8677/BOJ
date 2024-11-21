input=open(0).readline
for _ in range(int(input())):
    s,p=input().rstrip().split()
    p_len=len(p)
    i=0
    count=0
    while(i<len(s)):
        does_match=False
        if i+p_len<len(s)+1:
            for j in range(p_len):
                if s[i+j]==p[j]: does_match=True
                else: 
                    does_match=False
                    break
        if does_match: i+=p_len
        else: i+=1
        count+=1
    print(count)