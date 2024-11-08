#막대기 사이사이의 정보는 따로만들기 (한꺼번에 계산)
n=int(input())
h=list(map(int,input().split()))
surface=n*2 #윗면+밑면
surface+=sum(h)*2 #앞면+뒷면
if n==1:
    surface+=h[0]*2
    print(surface)
else:
    surface+=h[0]
    surface+=h[n-1]
    diff=[]
    for i in range(n-1): diff.append(abs(h[i]-h[i+1]))
    surface+=sum(diff)
    print(surface)