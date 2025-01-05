#PyPy 전용풀이
#뇌가 너무 말랑해진 나머지 이딴걸 40분이나 붙잡고 있다 -_-
for _ in range(int(input())):
    n,x,y=map(int,input().split()) #x=거리, y=부스터 최대치
    v_list=list(map(int,input().split())) #항상 n개만큼 들어옴
    z=0
    my_vel=v_list[n-1]
    done_wo_boost=False
    impossible=False
    times=[x/v_list[i] for i in range(n-1)]
    times.sort()
    mn=times[0]
    mx=times[n-2]
    while(z<=y):
        solo_win=True #solo_win=False 이면 단독우승X
        my_time=((x-z)/my_vel)
        if z>0: my_time+=1
        # print(f"my_time={my_time} when z={z}")
        #my_time의 범위 확인
        if my_time<mn: break
        else: solo_win=False
        # print(f"solo_win={solo_win}")
        if z==y and solo_win==False: 
            impossible=True
            break
        if z==0 and solo_win: done_wo_boost=True
        if solo_win: break
        z+=1
    if done_wo_boost: print(0)
    elif impossible: print(-1)
    else: print(z)