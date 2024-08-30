#Refined version (356ms)
s,p=map(int,input().split()) #String length, window length
dna_arr=input()
a,c,g,t=map(int,input().split())
dna_count={
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}
count=0
for i in range(p): dna_count[dna_arr[i]]+=1
for i in range(0,s-p+1):
    if dna_count["A"]>=a:
        if dna_count["C"]>=c:
            if dna_count["G"]>=g:
                if dna_count["T"]>=t:
                    count+=1
    dna_count[dna_arr[i]]-=1
    try: dna_count[dna_arr[i+p]]+=1
    except IndexError: continue
print(count)