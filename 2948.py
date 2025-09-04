#2009년 윤년 아님
#2009년은 목요일로 시작하는 해 -> T F S S M T W ...
#31 28 31 30 31 30 31 31 30 31 30 31
month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
d,m=map(int,input().split())
date=d+sum(month[:(m-1)]) if m>1 else d
print(week[date%7-1] if date>1 else week[0])
