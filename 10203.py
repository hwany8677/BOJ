input=open(0).readline
aeiou='aeiou'
for _ in range(int(input())):
    s=input().rstrip()
    count=0
    for c in s:
        if c in aeiou: count+=1
    print(f"The number of vowels in {s} is {count}.")
