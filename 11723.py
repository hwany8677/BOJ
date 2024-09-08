from sys import stdin
input=stdin.readline
seT={0}
m=int(input())
for _ in range(m):
    s=input().rstrip()
    try: cmd,x=s.split()
    except ValueError: cmd=s
    if cmd=="toggle":
        try: seT.remove(x)
        except KeyError: seT.add(x)
    if cmd=="add": seT.add(x)
    if cmd=="remove":
        try: seT.remove(x)
        except KeyError: continue
    if cmd=="check":
        print(int(x in seT))
    if cmd=="all":
        seT={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    if cmd=="empty":
        seT={0}