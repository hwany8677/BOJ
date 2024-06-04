for _ in range(int(input())):
    n=int(input()) #Repeats for n rounds -> e.g.) 1 2 3 4 5 -> 2 4 -> 3 -> 4 -> 5
    jailState=[0 for i in range(n)] #N Cells, 0 being 'locked'
    for i in range(1,n+1):
        for j in range(i,n+1,i): jailState[j-1]=0 if jailState[j-1] else 1
    print(sum(jailState))