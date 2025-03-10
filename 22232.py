#Sorting hiearchy -> filename first, extension after
#1. Filename (Lexi.)
#2. Recognized Extensions (Lexi.)
#3. Unrecognized Extensions (Lexi.)
input=open(0).readline
n,m=map(int,input().split())
buf=dict()
ext_known=[]
ext_unknown=[]
for _ in range(n):
    s=input().rstrip().split('.')
    name,ext=s[0],s[1]
    if name not in buf: buf[name]=[ext]
    else: buf[name].append(ext)
    ext_unknown.append(ext)
ext_unknown.sort()
for _ in range(m): 
    s=input().rstrip()
    if s in ext_unknown: ext_unknown.remove(s)
    ext_known.append(s)
ext_known.sort()
ext_keys=list(buf.keys())
ext_keys.sort()
buf={fname: buf[fname] for fname in ext_keys}
for element in buf.keys():
    for elemento in buf[element]: #buf[element] -> where all extensions go = elemento
        if elemento in ext_known: print(element,'.',elemento,sep='')
    for elemento in buf[element]:
        if elemento in ext_unknown: print(element,'.',elemento,sep='')
