bunja,bunmo=map(int,input().split())
while(not(bunmo==0 and bunja==0)):
    jungsu=bunja//bunmo
    bunja-=bunmo*jungsu
    print(f"{jungsu} {bunja} / {bunmo}")
    bunja,bunmo=map(int,input().split())