for _ in range(int(input())):
    n1=int(input())
    buf1=sorted(list(map(int,input().split())))
    n2=int(input())
    buf2=list(map(int,input().split()))
    for num in buf2:
        do_break=False
        start=0
        end=n1-1
        pos=(start+end)//2
        prev_pos=-1
        times_loop=0
        while(1):
            if prev_pos==pos: break
            if buf1[pos]==num or buf1[end]==num:
                print(1)
                do_break=True
                break
            elif buf1[pos]<num:
                prev_pos=pos
                start=pos
                pos=(start+end)//2
            elif buf1[pos]>num:
                prev_pos=pos
                end=pos
                pos=(start+end)//2
        if do_break: continue
        else: print(0)