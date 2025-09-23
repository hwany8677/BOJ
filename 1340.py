month={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
date=input().rstrip().split()
month_int=[31,28,31,30,31,30,31,31,30,31,30,31]
month_n=month[date[0]]
date[1]=date[1].split(',')[0]
year=int(date[2])
current_day=sum(month_int[:month_n-1])+int(date[1])-1 #-1 to exclude today
leap=True if year%400==0 or (year%4==0 and year%100!=0) else False
total_days=sum(month_int)+leap
if leap and month_n>2: current_day+=1
hour,min=map(int,date[3].split(':'))
current_min=current_day*1440+hour*60+min
total_in_min=total_days*1440
print(current_min/total_in_min*100)