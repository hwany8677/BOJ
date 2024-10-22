#zip == my savior, my light
#zip team_no and pos, sort team_no by pos, and put new position into a_pos by searching linearly
input=open(0).readline
r,c=map(int,input().split())
team_no=[0,1,2,3,4,5,6,7,8]
pos=[0,0,0,0,0,0,0,0,0] #raw position
for _ in range(r):
    buf=input().rstrip()
    for i in range(c):
        if buf[i].isnumeric():
            team=int(buf[i])-1
            pos[team]=i+2
            break
zipper=list(zip(team_no,pos))
zipper.sort(key=lambda x: x[1],reverse=True)
a_pos=[0,0,0,0,0,0,0,0,0]
prev_pos=-1
p=0
for element in zipper:
    team=element[0]
    if element[1]==prev_pos: a_pos[team]=p
    else:
        p+=1
        a_pos[team]=p
    prev_pos=element[1]
for num in a_pos: print(num)
