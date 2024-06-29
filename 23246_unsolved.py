#Screw lambda functions
#Hierarchy: pi->sigma->number (the smaller the better)
def product(lisT): #요소 內 곱연산
    pi=1
    for n in lisT: pi*=n
    return pi
n=int(input())
number=[]
pi=[]
sigma=[]
for i in range(n):
    buf=list(map(int,input().split()))
    number.append(buf[0])
    pi.append(product(buf[1:]))
    sigma.append(sum(buf[1:]))
pos=1
numberFinal=[]
for i in range(n): #pi 정렬 main
    pi_freq=dict()
    for num in pi: pi_freq[num]=0
    for num in pi: pi_freq[num]+=1
    pi_freq_value=[]
    i0=0
    for val in list(pi_freq.items()):
        pi_freq_value.append(val[i0][1])
        i0+=1
    pi_freq_value=sum(pi_freq_value)
    if pi_freq_value==len(pi): #pi_freq_value가 pi의 길이랑 같아야됨
        number.sort()
        print(*number)
        exit(0)
    else:
