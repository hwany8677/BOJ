str_to_find=input()
count=0
for _ in range(int(input())):
    s=input()
    s+=s
    if str_to_find in s: count+=1
print(count)