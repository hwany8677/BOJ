#should of, would of
#u, ur
#lol (even look for substring, like 'lolcat')
input=open(0).readline
for _ in range(int(input())):
    s=input().rstrip().split()
    wait=0
    wd_sd=0
    for word in s:
        if wd_sd:
            if word=="of": wait+=10
            wd_sd=0
        if "lol" in word: wait+=10
        if word=="u" or word=="ur": wait+=10
        if word=="would" or word=="should": wd_sd=1
    print(wait)
