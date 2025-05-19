#O(n^2)
input=open(0).readline
for _ in range(int(input())):
    k=int(input())
    buf=[]
    for _ in range(k): buf.append(input().rstrip())
    res="0"
    for i in range(k):
        for j in range(k):
            if i==j: continue
            cur=buf[i]+buf[j]
            not_pali=False
            for idx in range(len(cur)//2):
                if cur[idx]!=cur[len(cur)-1-idx]:
                    not_pali=True
                    break
            if not_pali: continue
            else: res=cur
    print(res)
