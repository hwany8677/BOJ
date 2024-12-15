#143 -> 1,4,3,14,43,143
#100 -> 0,1,10,100
#대충 int()돌렸을때 중복되는 내용은 빼면될듯
#슬라이딩 윈도우 + 이분탐색?
n=int(input())
d=list(map(str,input().split())) #중복 허용
found=[]
for window_size in range(1,n+1): #윈도우 크기만큼 시도
    for i in range(n-(window_size-1)):
        if i==0: #i==0일 때 윈도우 준비
            window=[d[i] for i in range(window_size)]
            res=''
            for number in window: res+=number
            found.append(int(res))
        else:
            window.append(d[i+window_size-1])
            res=''
            for idx in range(i,i+window_size):
                number=window[idx]
                res+=number
            found.append(int(res))
found=sorted(list(set(found)))
i=0
while(1):
    if i not in found:
        print(i)
        exit(0)
    i+=1
