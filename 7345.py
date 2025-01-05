#비트연산 응용 연습
input=open(0).readline
exp=[2**i for i in range(1994)]
def pi(poly):
    global exp
    poly_int=0
    mx_p=len(poly)
    for i in range(mx_p):
        bit=poly[i]
        if bit: poly_int+=exp[mx_p-1-i]
    return poly_int
def pi_reverse(poly_int):
    res_str=bin(poly_int)
    res=[]
    for i in range(2,len(res_str)): res.append(int(res_str[i]))
    return res
def add(poly1,poly2):
    poly1_int,poly2_int=pi(poly1),pi(poly2)
    # print(poly1_int,poly2_int)
    res=pi_reverse(poly1_int^poly2_int)
    return res
def mul(poly1,poly2):
    poly1_int,poly2_int=pi(poly1),pi(poly2)
    temp=0
    bit_pos=len(poly2)-1
    for bit in poly2:
        # if bit: print(bin((poly1_int<<bit_pos))*bit,bit_pos)
        temp^=((poly1_int)<<bit_pos)*bit
        bit_pos-=1
    # print(poly1_int,poly2_int,temp)
    res=pi_reverse(temp)
    return res
def solve(poly1,poly2): #poly1: 분자, poly2: 분모, poly3: 중간과정 다항식
    poly1_int,poly2_int=pi(poly1),pi(poly2)
    mx_p1,mx_p2=len(poly1),len(poly2) #실제 최고차수는 1을 빼줘야 나옴
    while(mx_p1>=mx_p2):
        to_shift=(mx_p1-mx_p2)
        # print(f"to_shift={to_shift}")
        poly3_int=poly2_int<<to_shift #몫 계산
        #뺄셈 시작
        poly3=pi_reverse(poly3_int)
        poly1_int=pi(add(poly1,poly3))
        #뺄셈 끝, 값 정리
        poly1=pi_reverse(poly1_int)
        mx_p1=len(poly1)
    return poly1
for _ in range(int(input())):
    f=list(map(int,input().split()))
    f.pop(0)
    g=list(map(int,input().split()))
    g.pop(0)
    h=list(map(int,input().split()))
    h.pop(0)
    i=mul(f,g)
    res=solve(i,h)
    print(len(res),end=' ')
    print(*res,sep=' ')