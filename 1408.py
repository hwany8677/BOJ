#무조건 정각이 되어서야'만' 시작!
current=input().split(":")
start=input().split(":")
for i in range(0,3):
	current[i]=int(current[i])
	start[i]=int(start[i])
cTime=3600*current[0]+60*current[1]+current[2]
sTime=3600*start[0]+60*start[1]+start[2]
if cTime>sTime: sTime+=86400
mTime=sTime-cTime
print(str(mTime//3600).zfill(2),':',str((mTime-(mTime//3600)*3600)//60).zfill(2),':',str((mTime-(mTime//3600)*3600-(((mTime-(mTime//3600)*3600)//60)*60))).zfill(2),sep='')
#print(current)
#print(start)
#print(cTime)
#print(sTime)

