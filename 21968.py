#흐어어 난 병신이다 이걸 삼진수가 안보이다니
#삼진수 -> 0,1,2
#삼진수 표현: 0,1,2,10,11,12,20,21,22,100,101,102,110,111,112,120,121,122,200,...
#십진수 표현: 0,1,2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,...
#하나씩 더하므로 1(3),10(3),11(3),100(3),101(3),110(3),111(3),...가 되어야함
#따라서 10진수로 받고 -> 2진수로 변환 -> 3진수로 읽기
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    res=''
    while(n>0):
        q=n//2
        r=n%2
        n=q
        res+=str(r)
    place=0
    for i in range(len(res)):
        digit=int(res[i])
        place+=digit*(3**i)
    print(place)