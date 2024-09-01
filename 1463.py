def check(num,mode): #1: Normal 2: 2로 나누기 잠금 3: 3으로 나누기 잠금
    count=0
    while(num>1):
        if mode!=3:
            n_div3=num//3
            n_div3_remainder=num%3
            if n_div3_remainder==0 and mode!=3:
                count+=1
                num//=3
                continue
        if mode!=2:
            n_div2=num//2
            n_div2_remainder=num%2
            if n_div2_remainder==0:
                count+=1
                num//=2
                continue
        count+=1
        num-=1
    return count
def check_2(num,mode): #서순 셔플
    count=0
    while(num>1):
        if mode!=2:
            n_div2=num//2
            n_div2_remainder=num%2
            if n_div2_remainder==0:
                count+=1
                num//=2
                continue
        count+=1
        num-=1
        if mode!=3:
            n_div3=num//3
            n_div3_remainder=num%3
            if n_div3_remainder==0 and mode!=3:
                count+=1
                num//=3
                continue
    return count
n=int(input())
tries=[]
#깡으로 확인, 1 빼보기, 2 빼보기
tries.append(check(n,1)); tries.append(check(n-1,1)+1); tries.append(check(n-2,1)+2) #0~2
tries.append(check(n,2)); tries.append(check(n-1,2)+1); tries.append(check(n-2,2)+2) #3~5
tries.append(check(n,3)); tries.append(check(n-1,3)+1); tries.append(check(n-2,3)+2) #6~8
tries.append(check_2(n,1)); tries.append(check_2(n-1,1)+1); tries.append(check_2(n-2,1)+2) #9~11
tries.append(check_2(n,2)); tries.append(check_2(n-1,2)+1); tries.append(check_2(n-2,2)+2) #12~14
tries.append(check_2(n,3)); tries.append(check_2(n-1,3)+1); tries.append(check_2(n-2,3)+2) #15~17
print(tries)
print(min(tries))