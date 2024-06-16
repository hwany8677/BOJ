#개날먹 (이게 실버5??)
dictionary=dict()
for _ in range(int(input())):
    a,b=input().split(' = ')
    dictionary[a]=b
for _ in range(int(input())):
    k=int(input())
    s=input().split()
    for c in s: print(dictionary[c],'',end='')
    print()