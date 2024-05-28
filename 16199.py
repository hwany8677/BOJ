#하나의 숫자로 계산.
"""
ex) ymd=20030123, sysmsd=20040124
sysmsd-ymd=10001, 만 나이=1=10001//10000
ymd=20030123, sysmsd=20030101
sysmsd-ymd<0, 만 나이=0
ymd=19700101, sysmsd=20240528
sysmsd-ymd=540427, 만 나이=54=540427//10000
ymd=20040229, sysmsd=20240229
sysmsd-ymd=200000, 만 나이=20=200000//10000
"""
y,m,d=map(int,input().split())
sy,sm,sd=map(int,input().split())
#만 나이
ymd=y*10000+m*100+d
sysmsd=sy*10000+sm*100+sd
print((sysmsd-ymd)//10000)
#세는 나이
print(sy-y+1)
#연 나이
print(sy-y)