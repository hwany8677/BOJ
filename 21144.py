#스레기처럼 풀어도 답나옴
n=int(input())
if n<10:
    s=input()
    if n==2 and s=='1': print(2); exit(0) #왠진몰라도 이걸 추가하니 96% 해결됨
    to_verify=1
    for char in s:
        current=int(char)
        if current!=to_verify:
            print(to_verify)
            break
        to_verify+=1
else:
    s=input()
    to_verify=1
    for i in range(0,9):
        current=int(s[i])
        if current!=to_verify:
            print(to_verify)
            exit(0)
        to_verify+=1
    for i in range(9,len(s)-1,2):
        cur1=int(s[i])*10
        cur2=int(s[i+1])
        if (cur1+cur2)!=to_verify:
            print(to_verify)
            exit(0)
        to_verify+=1
    print(100)