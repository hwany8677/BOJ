#Obstacle -> does not count as movement
#Therefore adds a bit of complexity for bruteforcing
#...or is it?
n,z,m=map(int,input().split())
if m>0:
    obstacle=list(map(int,input().split()))
    field=[(0 if i in obstacle else i) for i in range(1,n+1)]
    field=sorted(list(set(field)))
    field.remove(0)
else: field=[i for i in range(1,n+1)]
mn,k=999999999,0
for increment in range(1,len(field)-1):
    i=0
    count=0
    visited=[0]
    print(f"increment={increment}")
    while(field[i]!=z): 
        i+=increment
        if i>len(field)-1: i-=len(field)
        if i in visited: 
            print(f"i={i} already visited.")
            break
        visited.append(i)
        count+=g
        print(f"i={i}")
        input()
    print(f"'i's visited:",*visited,f", field[i]={field[i]}, i={i}, z={z}")
    if field[i]==z: 
        if count<=mn: 
            mn=count
            k=increment
            print(f"new mn={mn}, new k={k}")
            print(field)
print(k)
