#':' 기준으로 판단을해보자.
s=input()
ha,sa=0,0
for i in range(0,len(s)-1):
  if s[i]==':' and s[i+1]=='-':
    if s[i+2]==')': ha+=1
    elif s[i+2]=='(': sa+=1
print("happy" if ha>sa else "none" if ha==sa==0 else "sad" if ha<sa else "unsure")