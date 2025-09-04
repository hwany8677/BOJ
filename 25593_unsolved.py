#4시간, 6시간(10시간), 4시간(14시간), 10시간(24시간)
#시간 차이가 12시간 이하인데 추가하려고 하면 불공평을 즉시 때리기
#n주 뒤에 돌아오는 첫 스케쥴도 계산에 빠뜨리지 않기!
input=open(0).readline
n=int(input())
s=''
schedule=[]
week_schedule=[]
t=[4,6,4,10]
time_gaps=dict()
unfair=False
for _ in range(n):
    for i in range(4):
        current_t=t[i]
        s=input().rstrip().split()
        for element in s:
            if element=='-': continue
            else:
                if element not in time_gaps: time_gaps[element]=current_t
                else: 
                    if time_gaps[element]<
                    time_gaps[element]+=current_t
