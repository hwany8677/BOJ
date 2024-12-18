#0일 0시 0분 (기본 on) ~ 1000일 23시 59분
#1일=1440분, 1시간=60분
#15시, 18시, 21시
n,k=map(int,input().split())
# print(f"Target realtime={n*1440}")
m=0
realtime=0 #분단위
ac_time=0 #ac_time만 1440마다 리셋
when_shut=900
clock_freeze=0
while(realtime//1440!=n):
    if when_shut==ac_time: 
        if when_shut==900: when_shut=1080
        elif when_shut==1080: when_shut=1260
        elif when_shut==1260: 
            when_shut=900
            clock_freeze=k
    if clock_freeze==0: ac_time+=1
    else: clock_freeze-=1
    if ac_time==1440: ac_time=0
    realtime+=1
res=[]
# print(f"realtime={realtime}, ac_time={ac_time}, when_shut={when_shut}")
localtime=realtime-n*1440
while(realtime//1440==n):
    # print(f"localtime={localtime}")
    if when_shut==ac_time: 
        m+=1
        hh=localtime//60
        mm=localtime-hh*60
        res.append(f"{str(hh).zfill(2)}:{str(mm).zfill(2)}")
        if when_shut==900: when_shut=1080
        elif when_shut==1080: when_shut=1260
        elif when_shut==1260: 
            when_shut=900
            clock_freeze=k
    if clock_freeze==0: ac_time+=1
    else: clock_freeze-=1
    if ac_time==1440: ac_time=0
    realtime+=1
    localtime=realtime-n*1440
print(m)
for element in res: print(element)