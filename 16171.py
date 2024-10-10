#연속된 문자열이어야함
#1q2w3e4r! << qwer, qw, er, r!, we는 유효
#하지만 qe, wr, e!, qr와 같은, 떨어진 문자들은 해병-유효 (기열싸제어로 '유효하지 않음'이라 한다)
s=list(input())
k=input()
t=[]
for c in s:
    if c.isalpha(): t.append(c)
start=0
end=len(k)-1
while(end<len(t)):
    c=0
    for i in range(start,end+1): 
      if t[i]==k[i-start]: c+=1
    # print(f"start: {start} end: {end}")
    if c==len(k): break
    start+=1
    end+=1
print(1 if c==len(k) else 0)
