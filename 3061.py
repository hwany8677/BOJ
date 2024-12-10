#'최소한' '최대한' <<< 2147483648% 확률로 그리디
#끄에에에에ㅔㅔ에ㅔ에에ㅔ에에ㅔㅔㅔㅔㅔㄱ 왜애드혹없음? 왜애드혹없음? 왜애드혹없음? 왜애드혹없음?
#1 2 3 4
#1 3 2 4
#3 1 2 4
#3 2 1 4
#3 2 4 1
#사다리의 왼쪽 끝에 오도록 숫자를 다 밀기
#결론: 삽 입 정 렬
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    ladder_end=list(map(int,input().split()))
    buf=[i for i in range(1,n+1)]
    count=0
    for i in range(n):
        to_find=ladder_end[i]
        pos=buf.index(to_find)
        while(buf[i]!=to_find):
            buf[pos],buf[pos-1]=buf[pos-1],buf[pos]
            count+=1
            pos-=1
    print(count)