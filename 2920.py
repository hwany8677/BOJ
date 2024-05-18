#비교군과 비교방식
s=list(map(int,input().split()))
asc=list(s)
asc.sort()
des=list(asc)
des.reverse()
if s==asc: print("ascending")
if s==des: print("descending")
if s!=asc and s!=des: print("mixed")