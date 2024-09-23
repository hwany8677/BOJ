#Quick? Nah I'd bubble
# ^^^^^^^^^^^^ whoever wrote this bullshit must die istg
h=[]
for _ in range(0,9): h.append(int(input()))
h.sort()
for i in range(0,9):
    for j in range(i+1,9):
        sigma=0
        for k in range(0,9):
            if k==i or k==j: continue
            else: sigma+=h[k]
        if sigma==100:
            for k in range(0,9): 
                if k!=i and k!=j: print(h[k])
            exit(0)
