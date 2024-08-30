#Took 740ms on CPython (a bit messy)
#Sliding window?
dna={
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}
s,p=map(int,input().split()) #String length, window length
dna_arr=input()
req=list(map(int,input().split()))
dna_count=[0,0,0,0]
for i in range(p): dna_count[dna[dna_arr[i]]]+=1
count=0
if p==1:
    for i in range(s):
        if dna_count[i]>=req[i]: count+=1
        dna_count[dna[dna_arr[i]]]-=1
        if i!=s-1: dna_count[dna[dna_arr[i+1]]]+=1
else:
    start,end=0,p-1
    for i in range(0,s-p+1):
        temp=0
        for j in range(4): 
            if dna_count[j]>=req[j]: temp+=1
        #
        # 쓰고나니 드는 의문
        #
        if temp==4: count+=1
        dna_count[
            dna[
                dna_arr[start]
            ]
        ]-=1
        if i!=s-p:
            dna_count[
                dna[
                    dna_arr[end+1]
                ]
            ]+=1
        #
        # 이런 비효율적인 코드 구조를 어떻게 보면
        # 재귀 구조로 부를 수 있는건가? (∵ 인덱스 수식 안에 인덱스를 호출)
        #
        start+=1
        end+=1
print(count)