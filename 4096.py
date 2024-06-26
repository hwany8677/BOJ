# # ! ! refNum+=1 하지않고 더 빨리 찾을수있는 방법 없나 ! ! # #

#a[i:j:k]를 사용하면 list형임에 주의
#마라톤은 불랩제조기다...메모...
from math import ceil
while(1):
    n=input()
    if n=='0': break
    digits=len(n)
    cutPoint=int(digits/2) #실제 인덱스와 1 차이남에 유의
    left=n[:cutPoint]
    refNum=0
    #왼쪽이 전부 0인 경우 & 왼쪽에 뭐라도 있는 경우
    if int(''.join(left))==0: 
        refNum=(int(n)//(10**cutPoint))*(10**cutPoint)
        while(1):
            refNumStr=str(refNum).zfill(digits)
            # if refNumStr[:cutPoint]==refNumStr[digits-1:cutPoint:-1] and refNum>int(n): break
            match=0
            for i in range(digits):
                if refNumStr[i]==refNumStr[digits-1-i]: match+=1
            if match==digits and refNum>=int(n): break
            else: refNum+=10**(cutPoint-2)
            # print(refNumStr)
    else:
        # refNum=int(''.join(left)+''.join(left[::-1])) # < 반례: 21998을 빙빙돌아서 찾게됨 (02112 start)
        refNum=int(''.join(left)+('0' if ceil(digits/2)==cutPoint+1 else '')+''.join(left[::-1]))
        while(1):
            refNumStr=str(refNum).zfill(digits)
            # if refNumStr[:cutPoint]==refNumStr[digits-1:cutPoint:-1] and refNum>int(n): break
            match=0
            for i in range(digits):
                if refNumStr[i]==refNumStr[digits-1-i]: match+=1
            if match==digits and refNum>=int(n): break
            else: refNum+=1
            # print(refNumStr)
    # print(f"refNum: {refNumStr}")
    print(refNum-int(n))