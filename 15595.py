#딱봐도 해시맵 쓰라는 문제
#...근데 이 풀이가 맞나?
input=open(0).readline
n=int(input())
ac=0; wa=0
names=dict()
solve_status=[]
wa_count=[]
idx=0
for _ in range(n):
    buf=input().split()
    if buf[1]=='megalusion': continue
    if buf[1] not in names: 
        names[buf[1]]=idx
        wa_count.append(0)
        solve_status.append(0)
        idx+=1
    cur_name=names[buf[1]]
    if solve_status[cur_name]==0: 
        if buf[2]=='4': 
            ac+=1
            wa+=wa_count[cur_name]
            solve_status[cur_name]=1
        else: wa_count[cur_name]+=1
try: 
    rate=(ac/(ac+wa))*100
    if rate==0.0: rate=0
except ZeroDivisionError: rate=0
print(rate)