#이게 왜 DP 붙어있는지 이해를 할수가 없음
#C H J E M R
#1 
alpha=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1] #65를 빼야함
a=input()
b=input()
buf=[]
for i in range(len(a)):
    buf.append(alpha[ord(a[i])-65])
    buf.append(alpha[ord(b[i])-65])
length=len(buf)
while(length>2):
    for i in range(length-1):
        buf[i]=(buf[i]+buf[i+1])%10
    length-=1
print(buf[0],buf[1],sep='')