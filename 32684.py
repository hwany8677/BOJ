#No-brainer code
buf1=list(map(int,input().split()))
buf2=list(map(int,input().split()))
sigma1=buf1[0]*13+buf1[1]*7+buf1[2]*5+buf1[3]*3+buf1[4]*3+buf1[5]*2
sigma2=buf2[0]*13+buf2[1]*7+buf2[2]*5+buf2[3]*3+buf2[4]*3+buf2[5]*2
sigma2+=1.5
if sigma1>sigma2: print("cocjr0208")
else: print("ekwoo")
